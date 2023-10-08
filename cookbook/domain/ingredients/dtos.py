from typing import Optional
from pydantic import BaseModel


class IngredientWriteDTO(BaseModel):
    name: str
    unit: Optional[str] = None
    shelve: str


class IngredientReadDTO(IngredientWriteDTO):
    uid: str
