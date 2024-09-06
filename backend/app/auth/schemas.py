from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from fastapi_users import schemas



class UserBaseSchema(schemas.BaseUserCreate):
    username: str = Field(..., min_length=2, max_length=50)
    email: EmailStr = Field(..., max_length=256)
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserSchema(UserBaseSchema):
    id: int


class UserCreateSchema(UserBaseSchema):
    password: str = Field(..., min_length=8, max_length=50)
    # многоточие - если нет дефолтного значения
    # пароль здесь, чтобы не возвращался к юзеру


class UserRead(schemas.BaseUser[int]):
    id: int
    username: str = Field(..., min_length=2, max_length=50)
    email: EmailStr = Field(..., max_length=256)
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
