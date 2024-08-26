from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from ..database import get_session
from ..schemas.recipe import RecipeCreateSchema, RecipeSchema
from ..services.recipe import create_recipe


router = APIRouter(prefix="/recipe", tags=["recipe"])


@router.post("/recipe", response_model=RecipeSchema)
async def new_recipe(
        user: RecipeCreateSchema,  session: Session = Depends(get_session)
):
    """Registration of new user"""
    try:
        return create_recipe(session, user)
    except IntegrityError:
        raise HTTPException(status_code=422, detail='User already exists')