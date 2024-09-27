from sqlalchemy import String, Text, ForeignKey, Integer, JSON, Boolean
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing_extensions import Annotated

from backend.database import Base


class Recipes(Base):
    __tablename__ = 'recipes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), unique=True)
    description: Mapped[str] = mapped_column(String(256))
    instruction: Mapped[str] = mapped_column(String(256))
    cook_time: Mapped[int] = mapped_column(Integer)
    calories: Mapped[int] = mapped_column(Integer)

    meal_type: Mapped[str] = mapped_column(String(25))
    diet_type: Mapped[str] = mapped_column(String(25))

    image_url: Mapped[str] = mapped_column(String)
    # связи
    # foodstuffs: ..
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    creator = relationship("User", back_populates="recipes")
