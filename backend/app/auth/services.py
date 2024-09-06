from sqlalchemy.orm import Session

from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi import Depends

from backend.app.auth.schemas import UserCreateSchema
from backend.app.auth.models import User
from backend.database import get_async_session


def create_user(session: Session, user: UserCreateSchema) -> User:
    user_model = User(**user.model_dump())

    session.add(user_model)
    session.commit()
    session.refresh(user_model)

    return user_model  # возвращаем пользователя


def get_user(session: Session = Depends(get_async_session)) -> User:
    yield SQLAlchemyUserDatabase(session, User)