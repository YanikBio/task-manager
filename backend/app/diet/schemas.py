from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from fastapi_users import schemas


class DietBaseSchema(BaseModel):
    title: str = Field(..., min_length=2, max_length=50)
    description: str = Field(..., min_length=2, max_length=256)


class DietSchema(DietBaseSchema):
    id: int


class DietCreateSchema(DietBaseSchema):
    pass
    # многоточие - если нет дефолтного значения
    # пароль здесь, чтобы не возвращался к юзеру

