from typing import List

from fastapi import APIRouter

from cookbook.domain.ingredients.repository import IngredientRepository
from cookbook.domain.recipes.dtos import (
    RecipeDetailsDTO,
    RecipeIngredientReadDTO,
    RecipeIngredientWriteDTO,
    RecipeReadDTO,
    RecipeWriteDTO,
)
from cookbook.domain.recipes.repository import RecipeRepository

router = APIRouter()
recipe_repository = RecipeRepository()
ingredient_repository = IngredientRepository()


@router.post("/recipes", response_model=RecipeReadDTO)
async def create_recipe(recipe_create_dto: RecipeWriteDTO):
    return recipe_repository.create(recipe_create_dto)


@router.get("/recipes", response_model=List[RecipeReadDTO])
async def search_recipes():
    return recipe_repository.search()


@router.get("/recipes/{recipe_uid}", response_model=RecipeDetailsDTO)
async def get_recipe_details(recipe_uid: str):
    return recipe_repository.get_by_uid(recipe_uid)


@router.post(
    "/recipes/{recipe_uid}/ingredients", response_model=RecipeIngredientReadDTO
)
async def recipe_add_ingredient_quantity(
    recipe_uid: str, recipe_ingredient_dto: RecipeIngredientWriteDTO
):
    data = recipe_ingredient_dto.dict()
    recipe = recipe_repository.get_by_uid(recipe_uid)
    ingredient = ingredient_repository.get_by_uid(data.pop("ingredient_uid"))
    return recipe_repository.add_ingredient(recipe, ingredient, **data)
