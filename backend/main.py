from fastapi import FastAPI
from backend.app.handlers import auth
from backend.app.handlers import recipe

app = FastAPI()
app.include_router(auth.router, prefix="/api/v1")
app.include_router(recipe.router, prefix="/api/v1")
