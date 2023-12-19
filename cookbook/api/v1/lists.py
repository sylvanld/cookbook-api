from typing import List

from fastapi import APIRouter

from cookbook.domain.groups.repository import GroupRepository
from cookbook.domain.lists.dtos import ListRecipeReadDTO, ListRecipeWriteDTO
from cookbook.domain.lists.repository import ListRepository
from cookbook.domain.recipes.repository import RecipeRepository

router = APIRouter()
group_repository = GroupRepository()
recipe_repository = RecipeRepository()
list_repository = ListRepository()


@router.get("/groups/{group_uid}/list/recipes", response_model=List[ListRecipeReadDTO])
async def get_list(group_uid: str):
    group = group_repository.get_by_uid(group_uid)
    return list_repository.get_recipes(group)


@router.post("/groups/{group_uid}/list/recipes", response_model=ListRecipeReadDTO)
async def add_recipe_to_list(group_uid: str, list_recipe_dto: ListRecipeWriteDTO):
    group = group_repository.get_by_uid(group_uid)
    recipe = recipe_repository.get_by_uid(list_recipe_dto.recipe_uid)
    return list_repository.add_recipe(group, recipe, diners=list_recipe_dto.diners)
