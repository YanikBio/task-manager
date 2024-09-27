from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from fastapi_users import schemas


class RecipeBaseSchema(BaseModel):
    title: str = Field(..., min_length=2, max_length=50)
    description: str = Field(..., min_length=2, max_length=256)
    instruction: str = Field(..., min_length=2, max_length=256)
    cook_time: int
    calories: int

    meal_type: str = Field(..., min_length=5, max_length=20)
    diet_type: str = Field(..., min_length=5, max_length=20)


class RecipeSchema(RecipeBaseSchema):
    id: int


class RecipeCreateSchema(RecipeBaseSchema):
    pass
    # многоточие - если нет дефолтного значения
    # пароль здесь, чтобы не возвращался к юзеру


