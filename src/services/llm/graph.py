from langchain_core.messages import HumanMessage,ToolMessage
from langgraph.graph import StateGraph, END, START
from src.services.llm.state_graph import GraphState
from src.services.llm.nodes import Nodes
from src.services.llm.tools import tool_list
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import AIMessage,AIMessageChunk
from langchain_core.messages import trim_messages
from langgraph.checkpoint.postgres import PostgresSaver
from src.config.settings import settings
from contextlib import contextmanager
from src.services.llm.save_user_messages import create_or_save_message
from sqlalchemy.types import UUID
import uuid


db_url = settings.database_url.replace(
    "postgresql+psycopg://",
    "postgresql://",
)


@contextmanager
def get_checkpointer():

    with PostgresSaver.from_conn_string(db_url) as checkpointer:
        yield checkpointer



def limit_messages(messages):
    return trim_messages(
        messages,
        max_tokens=5000,
        token_counter="approximate",
        strategy="last",
        start_on="human",
        include_system=True,
        allow_partial=False,
    )

def graph_build(checkpointer):
    graph = StateGraph(GraphState)
    nodes = Nodes()
    tools = ToolNode(tool_list)
    
    
    graph.add_node("llm_agent", nodes.call_llm)
    graph.add_node("tools", tools)

    graph.add_edge(START, "llm_agent")
    graph.add_conditional_edges(
        "llm_agent",
        tools_condition,
        ["tools", END]
    )
    graph.add_edge("tools", "llm_agent")

    compailed_graph = graph.compile(checkpointer=checkpointer)
    print(compailed_graph)  
    return compailed_graph



def invoke_graph(query: str, session_id: UUID):
    with get_checkpointer() as checkpointer:

        checkpointer.setup()

        graph = graph_build(checkpointer)

        config = {
            "configurable": {
                "thread_id": str(session_id)
            }
        }


        create_or_save_message(sesson_id=session_id, role="user", message=query)
        assistant_response=[]

        for chunk, metadata in graph.stream(
            {"messages": [HumanMessage(content=query)]},
            stream_mode="messages",
            config=config
        ):

            node = (
                metadata.get("langgraph_node")
                if isinstance(metadata, dict)
                else metadata
            )

            print("NODE:", node)
            print("TYPE:", type(chunk).__name__)
            print("CONTENT:", repr(str(chunk.content)))

            # Tool call
            if getattr(chunk, "tool_calls", None):
                print(f"[{node}] Tool requested:")
                print(chunk.tool_calls)

            if isinstance(chunk, ToolMessage):

                create_or_save_message(
                    sesson_id=session_id,
                    role="tool",
                    message=str(chunk.content),
                )
            # Only stream actual text
            if isinstance(chunk, AIMessageChunk):
                if isinstance(chunk.content, str) and chunk.content:
                    assistant_response.append(
                        chunk.content
                    )
                    yield chunk.content
        
        create_or_save_message(sesson_id=str(session_id), role="assistant", message="".join(assistant_response))