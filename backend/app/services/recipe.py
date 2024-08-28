from sqlalchemy.orm import Session

from ..schemas.recipe import RecipeCreateSchema, RecipeSchema
from ..models import Recipe


def create_recipe(session: Session, recipe: RecipeCreateSchema) -> Recipe:
    recipe_model = Recipe(**recipe.model_dump())

    session.add(recipe_model)
    session.commit()
    session.refresh(recipe_model)

    return recipe_model  # возвращаем рецепт


def show_recipes(session: Session, user):
    ...