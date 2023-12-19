from pydantic import BaseModel

from cookbook.domain.recipes.dtos import RecipeReadDTO


class ListRecipeWriteDTO(BaseModel):
    recipe_uid: str
    diners: int


class ListRecipeReadDTO(BaseModel):
    diners: int
    recipe: RecipeReadDTO
