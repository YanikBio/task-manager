from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
# from fastapi_users import fastapi_users

from backend.app.auth.models import User
# from backend.app.handlers import auth
# from backend.app.handlers import recipe
from backend.app.auth.base_config import auth_backend, fastapi_users
from backend.app.auth.schemas import UserCreateSchema, UserRead

app = FastAPI()
# app.include_router(auth.router, prefix="/api/v1")
# app.include_router(recipe.router, prefix="/api/v1")
#
# fastapi_users = FastAPIUsers[User, int](
#     get_user_manager,
#     [auth_backend],
# )

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreateSchema),
    prefix="/auth",
    tags=["auth"],
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


current_user = fastapi_users.current_user()


# Get the current user (active or not)
@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello"