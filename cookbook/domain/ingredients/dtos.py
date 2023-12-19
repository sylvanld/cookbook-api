from enum import Enum
from typing import Optional

from pydantic import BaseModel


class Shelve(Enum):
    BAKERY = "bakery"
    BUTCHER = "butcher"
    CHEESE = "cheese"
    FISH = "fish"
    GROCERY = "grocery"
    PATISSERIE = "patisserie"
    POULTRY = "poultry"
    SAUSAGE = "sausage"
    SPICES = "spices"
    VEGETABLES = "vegetables"


class IngredientWriteDTO(BaseModel):
    class Config:
        use_enum_values = True

    name: str
    shelve: Shelve
    unit: Optional[str] = None
    thumbnail_url: Optional[str] = None


class IngredientReadDTO(IngredientWriteDTO):
    uid: str
    name: str
    shelve: Shelve
    unit: Optional[str] = None
    thumbnail_url: Optional[str] = None
