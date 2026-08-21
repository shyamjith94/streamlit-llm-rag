from src.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String

class User(BaseModel):
    __tablename__ = "users"
    name:Mapped[str] = mapped_column(String(100), nullable=False)
    email:Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    password:Mapped[str] = mapped_column(String(100), nullable=False)