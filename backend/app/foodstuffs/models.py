from sqlalchemy import String, Text, ForeignKey, Integer, JSON, Boolean
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing_extensions import Annotated

from backend.database import Base


class Foodstuffs(Base):
    __tablename__ = 'foodstuffs'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), unique=True)
    description: Mapped[str] = mapped_column(String(256))