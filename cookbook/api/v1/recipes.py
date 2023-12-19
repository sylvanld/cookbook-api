from typing import List

from fastapi import APIRouter, Depends

from cookbook.domain.ingredients.repository import IngredientRepository
from cookbook.domain.recipes.dtos import (
    RecipeDetailsDTO,
    RecipeIngredientReadDTO,
    RecipeIngredientWriteDTO,
    RecipeReadDTO,
    RecipeWriteDTO,
)
from cookbook.domain.recipes.query import RecipeQuery
from cookbook.domain.recipes.repository import RecipeRepository

router = APIRouter()
recipe_repository = RecipeRepository()
ingredient_repository = IngredientRepository()


@router.post("/recipes", response_model=RecipeReadDTO)
async def create_recipe(recipe_create_dto: RecipeWriteDTO):
    return recipe_repository.create(recipe_create_dto)


@router.put("/recipes/{recipe_uid}", response_model=RecipeReadDTO)
async def update_recipe(recipe_uid: str, recipe_create_dto: RecipeWriteDTO):
    recipe = recipe_repository.get_by_uid(recipe_uid)
    return recipe_repository.update(recipe, recipe_create_dto)


@router.get("/recipes", response_model=List[RecipeReadDTO])
async def search_recipes(query: RecipeQuery = Depends(RecipeQuery.from_request)):
    return recipe_repository.search(query)


@router.get("/recipes/{recipe_uid}", response_model=RecipeDetailsDTO)
async def get_recipe_details(recipe_uid: str):
    return recipe_repository.get_by_uid(recipe_uid)


@router.delete("/recipes/{recipe_uid}", status_code=202)
async def delete_recipe(recipe_uid: str):
    recipe = recipe_repository.get_by_uid(recipe_uid)
    recipe_repository.delete(recipe)


@router.post("/recipes/{recipe_uid}/ingredients", response_model=RecipeIngredientReadDTO)
async def recipe_add_ingredient_quantity(recipe_uid: str, recipe_ingredient_dto: RecipeIngredientWriteDTO):
    data = recipe_ingredient_dto.dict()
    recipe = recipe_repository.get_by_uid(recipe_uid)
    ingredient = ingredient_repository.get_by_uid(data.pop("ingredient_uid"))
    return recipe_repository.add_ingredient(recipe, ingredient, **data)


@router.put(
    "/recipes/{recipe_uid}/ingredients/{recipe_ingredient_uid}", response_model=RecipeIngredientReadDTO, status_code=200
)
async def recipe_update_ingredient(
    recipe_uid: str, recipe_ingredient_uid: str, recipe_ingredient_dto: RecipeIngredientWriteDTO
):
    recipe_repository.get_by_uid(recipe_uid)

    data = recipe_ingredient_dto.dict()
    data["ingredient"] = ingredient_repository.get_by_uid(data.pop("ingredient_uid"))

    recipe_ingredient = recipe_repository.get_ingredient(recipe_ingredient_uid)
    return recipe_repository.update_ingredient(recipe_ingredient, **data)


@router.delete("/recipes/{recipe_uid}/ingredients/{recipe_ingredient_uid}", status_code=202)
async def recipe_delete_ingredient(recipe_uid: str, recipe_ingredient_uid: str):
    # verify that recipe exists
    recipe_repository.get_by_uid(recipe_uid)

    ingredient = recipe_repository.get_ingredient(recipe_ingredient_uid)
    recipe_repository.delete_ingredient(ingredient)
