from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from datetime import datetime

class BaseModel(DeclarativeBase):
    """Base model for all models"""
    id:Mapped[int] = mapped_column(primary_key=True)
    created_date:Mapped[datetime] = mapped_column(default=datetime.now())
    updated_date:Mapped[datetime] = mapped_column(default=datetime.now())
    