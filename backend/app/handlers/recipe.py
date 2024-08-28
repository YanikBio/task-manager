from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from ..database import get_session
from ..schemas.recipe import RecipeCreateSchema, RecipeSchema
from ..services.recipe import create_recipe


router = APIRouter(prefix="/recipe", tags=["recipe"])


@router.post("/recipe", response_model=RecipeSchema)
async def new_recipe(
        recipe: RecipeCreateSchema,  session: Session = Depends(get_session)
):
    """Registration of new recipe"""
    try:
        return create_recipe(session, recipe)
    except IntegrityError:
        raise HTTPException(status_code=422, detail='Recipe already exists')


# @router.get("/recipe", response_model=RecipeSchema)
# async def get_user_recipes(
#         user_id: int,
# ):
#     if user_id not in users_recipes:
#         raise HTTPException(status_code=404, detail="Пользователь не найден")
#     return users_recipes[user_id]