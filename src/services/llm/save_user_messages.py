from src.config.db import get_db
from src.models import ChatSessions, ChatMessages
from src.st_state import get_user_info
from typing import Optional
from sqlalchemy.types import UUID

def create_or_save_session(sesson_id:UUID, title:Optional[str] = None):
    user_info = get_user_info()
    if user_info is None:
        raise ValueError("User information is not available")
    with get_db() as db:
        try:
            chat_session = ChatSessions(session_id=sesson_id, title="test session", user_id=user_info.id)
            db.add(chat_session)
            db.commit()
            db.refresh(chat_session)
        except Exception as exe:
            print(f"create or save user session error {exe}")
            db.rollback()
            raise exe

def create_or_save_message(sesson_id:UUID, role:str, message:str):
    user_info = get_user_info()
    if user_info is None:
        raise ValueError("User information is not available")
    with get_db() as db:
        try:
            chat_message = ChatMessages(session_id=sesson_id, message=message, role=role, user_id=user_info.id)
            db.add(chat_message)
            db.commit()
            db.refresh(chat_message)
        except Exception as exe:
            print(f"create or save user message error {exe}")
            db.rollback()
            raise exe