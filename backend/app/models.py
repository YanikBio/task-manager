from sqlalchemy import String, Text, ForeignKey
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
    recipe = relationship('Post', back_populates='user', lazy='select')  # как это поняточки


class Recipe(Base):
    __tablename__ = 'recipes'

    # Колонки
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(256))
    describe: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))  # обрати внимание, идентификатор таблицы, а не класса
    # Связи
    user: Mapped[User] = relationship('User', back_populates='recipes')