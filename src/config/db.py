from sqlalchemy import create_engine
from src.config.settings import settings
from sqlalchemy.orm import Session, sessionmaker
from contextlib import contextmanager
from typing import Generator

engine = create_engine(
    settings.database_url,
    echo=False,
    pool_size=10,
    max_overflow=20,
)

session_local = sessionmaker(
    bind=engine,
    class_=Session,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

@contextmanager
def get_db() -> Generator[Session, None, None]:
    db = session_local()
    try:
        yield db
    finally:
        db.close()
