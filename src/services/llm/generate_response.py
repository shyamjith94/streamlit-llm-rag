from src.services.llm import get_llm_client
from langchain_core.messages import HumanMessage

def get_response(query:str):
    llm = get_llm_client()
    for chunk in llm.stream(query):
        yield chunk


