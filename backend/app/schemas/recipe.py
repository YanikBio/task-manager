from pydantic import BaseModel, Field, EmailStr
from typing import List, Dict, Any



class RecipeBaseSchema(BaseModel):
    title: str = Field(..., min_length=2, max_length=50)
    describe: str = Field(..., min_length=2, max_length=256)

    ingredients: Dict[str, Any] = Field(..., min_length=1)

    instructions: str = Field(..., min_length=2)  # Изменено с Mapped[str] на str
    prep_time: int = Field(..., ge=0)  # Время приготовления не может быть отрицательным
    cook_time: int = Field(..., ge=0)  # Время готовки не может быть отрицательным
    total_time: int = Field(..., ge=0)  # Общее время не может быть отрицательным
    servings: int = Field(..., ge=1)  # Количество порций должно быть положительным

class RecipeSchema(RecipeBaseSchema):
    id: int


class RecipeCreateSchema(RecipeBaseSchema):
    ...
    # password: str = Field(..., min_length=8, max_length=50)
    # многоточие - если нет дефолтного значения
    # пароль здесь, чтобы не возвращался к юзеру