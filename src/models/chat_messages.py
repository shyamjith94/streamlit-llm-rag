from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String,Text
from src.models.base import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.sql.sqltypes import UUID

class ChatMessages(BaseModel):
    __tablename__ = "chat_messages"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    session_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("chat_sessions.session_id"),
        nullable=False,
        index=True
    )

    role: Mapped[str] = mapped_column(
        String(10),
        nullable=False
    )

    message: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    chat_session: Mapped["ChatSessions"] = relationship(
        back_populates="chat_messages"
    )