from typing import List, Optional

from pydantic import BaseModel


class IngredientReadDTO(BaseModel):
    uid: str
    name: str
    thumbnail_url: Optional[str] = None


class RecipeIngredientWriteDTO(BaseModel):
    ingredient_uid: str
    quantity: Optional[float] = None
    unit: Optional[str] = None


class RecipeIngredientReadDTO(BaseModel):
    uid: str
    quantity: Optional[float] = None
    unit: Optional[str] = None
    ingredient: IngredientReadDTO


class RecipeReadDTO(BaseModel):
    uid: str
    name: str
    diners: int
    is_public: bool
    price: float
    duration_minutes: int
    ingredient_names: List[str]

    description: Optional[str]
    thumbnail_url: Optional[str]


class RecipeWriteDTO(BaseModel):
    name: str
    diners: int
    price: float
    duration_minutes: int

    description: Optional[str] = None
    thumbnail_url: Optional[str] = None
    is_public: bool = True


class RecipeDetailsDTO(RecipeReadDTO):
    ingredients: List[RecipeIngredientReadDTO]
