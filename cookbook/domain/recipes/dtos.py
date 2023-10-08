from typing import List

from pydantic import BaseModel


class IngredientReadDTO(BaseModel):
    uid: str
    name: str


class RecipeIngredientWriteDTO(BaseModel):
    ingredient_uid: str
    quantity: float = None
    unit: str = None


class RecipeIngredientReadDTO(BaseModel):
    uid: str
    quantity: float = None
    unit: str = None
    ingredient: IngredientReadDTO


class RecipeReadDTO(BaseModel):
    uid: str
    name: str
    diners: int
    is_public: bool


class RecipeWriteDTO(BaseModel):
    name: str
    diners: int
    is_public: bool = False


class RecipeDetailsDTO(RecipeReadDTO):
    ingredients: List[RecipeIngredientReadDTO]
