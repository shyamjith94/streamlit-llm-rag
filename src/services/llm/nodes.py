from src.services.llm import get_llm_client
from src.services.llm.state_graph import GraphState
from src.services.llm.tools import tool_list
from langchain_core.messages import SystemMessage
from src.services.llm import SYSTEM_PROMPT


class Nodes:
   
    def __init__(self):
        # self.state = GraphState()
        self.llm = get_llm_client()
        self.llm_with_tools = self.llm.bind_tools(tool_list)
    
    def call_llm(self, state:GraphState):
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            *state.messages
        ]
        response = self.llm_with_tools.invoke(messages)
        return {"messages":[response]}