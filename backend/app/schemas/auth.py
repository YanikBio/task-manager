from pydantic import BaseModel, Field, EmailStr



class UserBaseSchema(BaseModel):
    username: str = Field(..., min_length=2, max_length=50)
    email: EmailStr = Field(..., max_length=256)


class UserSchema(UserBaseSchema):
    id: int


class UserCreateSchema(UserBaseSchema):
    password: str = Field(..., min_length=8, max_length=50)
    # многоточие - если нет дефолтного значения
    # пароль здесь, чтобы не возвращался к юзеру