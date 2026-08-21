from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, END, START
from src.services.llm.state_graph import GraphState
from src.services.llm.nodes import Nodes
from src.services.llm.tools import tool_list
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import AIMessage,AIMessageChunk
def graph_build():
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

    compailed_graph = graph.compile()
    print(compailed_graph)
    return compailed_graph

def invoke_graph(query: str):
    graph = graph_build()

    for chunk, metadata in graph.stream(
        {"messages": [HumanMessage(content=query)]},
        stream_mode="messages",
    ):

        node = (
            metadata.get("langgraph_node")
            if isinstance(metadata, dict)
            else metadata
        )

        print("NODE:", node)
        print("TYPE:", type(chunk).__name__)
        print("CONTENT:", repr(chunk.content))

        # Tool call
        if getattr(chunk, "tool_calls", None):
            print(f"[{node}] Tool requested:")
            print(chunk.tool_calls)

        # Only stream actual text
        if isinstance(chunk, AIMessageChunk):
            if isinstance(chunk.content, str) and chunk.content:
                yield chunk.content