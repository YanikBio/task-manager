from sqlalchemy.orm import Session

from ..schemas.auth import UserCreateSchema, UserSchema
from ..models import User


def create_user(session: Session, user: UserCreateSchema) -> User:
    user_model = User(**user.model_dump())

    session.add(user_model)
    session.commit()
    session.refresh(user_model)

    return user_model  # возвращаем пользователя