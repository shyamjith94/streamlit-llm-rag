import streamlit as st
from pydantic.dataclasses import dataclass as pdddataclass,Field
from typing import Optional

@pdddataclass
class AgentChatMessage:
    messages:list[dict[str, str]] = Field(default_factory=list)
    suggestions:bool = True
    


@pdddataclass
class UserData:
    id:Optional[int]= None
    name:str = ""
    email:str = ""
    logged_in:bool = False
    session_id:Optional[str]=None


