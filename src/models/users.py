from __future__ import annotations
from src.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy.types import String
from typing import List

class Users(BaseModel):
    __tablename__ = "users"
    name:Mapped[str] = mapped_column(String(100), nullable=False)
    email:Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    password:Mapped[str] = mapped_column(String(100), nullable=False)


    chat_sessions:Mapped[list["ChatSessions"]] = relationship(back_populates="user")
    