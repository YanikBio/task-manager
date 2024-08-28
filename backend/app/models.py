from sqlalchemy import String, Text, ForeignKey, Integer, JSON
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing_extensions import Annotated

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50), unique=True)
    # Связь
    recipe = relationship('Recipe', back_populates='user', lazy='select')  # как это поняточки


class Recipe(Base):
    __tablename__ = 'recipes'

    # Колонки
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(256))
    describe: Mapped[str] = mapped_column(Text)

    ingredients: Mapped[dict] = mapped_column(JSON, nullable=False)  # JSON или текстовое поле?
    instructions: Mapped[str] = mapped_column(Text, nullable=False)
    prep_time: Mapped[int] = mapped_column(Integer)  # Время приготовления в минутах
    cook_time: Mapped[int] = mapped_column(Integer)  # Время готовки в минутах
    total_time: Mapped[int] = mapped_column(Integer)  # Общее время в минутах
    servings: Mapped[int] = mapped_column(Integer)  # Количество порций

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))  # обрати внимание, идентификатор таблицы, а не класса
    # Связи
    user: Mapped[User] = relationship('User', back_populates='recipe')
