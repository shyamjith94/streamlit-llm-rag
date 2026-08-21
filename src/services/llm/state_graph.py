from typing import Annotated
import operator
from langchain_core.messages import BaseMessage
from pydantic import BaseModel

class GraphState(BaseModel):
    messages: Annotated[list[BaseMessage],operator.add]


    