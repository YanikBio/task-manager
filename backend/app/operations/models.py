from sqlalchemy import String, Text, ForeignKey, Integer, JSON, Boolean, TIMESTAMP
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime
from typing_extensions import Annotated

from backend.database import Base, SQLAlchemyBaseUserTable


class User(Base):
    __tablename__ = 'operations'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    quantity: Mapped[str] = mapped_column(String(50))
    figi: Mapped[str] = mapped_column(String(50))
    instrument_type: Mapped[str] = mapped_column(String(50), nullable=True)
    data: Mapped[datetime] = mapped_column(TIMESTAMP)
    type: Mapped[str] = mapped_column(TIMESTAMP)
