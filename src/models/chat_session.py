from sqlalchemy.sql.sqltypes import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import BaseModel
from sqlalchemy import ForeignKey,String


class ChatSessions(BaseModel):
    __tablename__ = "chat_sessions"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    session_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
        unique=True,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    user: Mapped["Users"] = relationship(
        back_populates="chat_sessions"
    )

    chat_messages: Mapped[list["ChatMessages"]] = relationship(
        back_populates="chat_session"
    )
    