from pydantic import BaseModel, Field, EmailStr



class RecipeBaseSchema(BaseModel):
    title: str = Field(..., min_length=2, max_length=50)
    describe: str = Field(..., min_length=2, max_length=256)


class RecipeSchema(RecipeBaseSchema):
    id: int


class RecipeCreateSchema(RecipeBaseSchema):
    ...
    # password: str = Field(..., min_length=8, max_length=50)
    # многоточие - если нет дефолтного значения
    # пароль здесь, чтобы не возвращался к юзеру