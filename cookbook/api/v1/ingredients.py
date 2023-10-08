from typing import List
from fastapi import APIRouter, Query

from cookbook.domain.ingredients.dtos import IngredientReadDTO, IngredientWriteDTO
from cookbook.domain.ingredients.repository import IngredientRepository

router = APIRouter()
ingredient_repository = IngredientRepository()

@router.get("/ingredients", response_model=List[IngredientReadDTO])
async def search_ingredients(name: str = Query(...)):
    return ingredient_repository.search(name=name)


@router.post("/ingredients", response_model=IngredientReadDTO)
async def create_ingredient(ingredient_create_dto: IngredientWriteDTO):
    return ingredient_repository.create(ingredient_create_dto)

@router.put("/ingredients/{ingredient_uid}", response_model=IngredientReadDTO)
async def update_ingredient(ingredient_uid: str, ingredient_update_dto: IngredientWriteDTO):
    ingredient = ingredient_repository.get_by_uid(ingredient_uid)
    return ingredient_repository.update(ingredient, ingredient_update_dto)
