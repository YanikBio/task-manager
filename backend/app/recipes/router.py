from fastapi import APIRouter, Depends


from .schemas import RecipeCreateSchema
from backend.app.auth.base_config import current_user
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_async_session
from backend.app.auth.models import User

router = APIRouter(
    prefix="/recipes",
    tags=["Recipes"]
)


@router.post("/new_recipe", response_model=RecipeCreateSchema)
async def add_new_recipe(
        user: User = Depends(current_user),

):
    ...


@router.post("/show_recipe")
async def show_all_recipe(user: User = Depends(current_user)):
    ...
