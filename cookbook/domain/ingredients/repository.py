from fastapi import HTTPException
from cookbook.core.identifiers import generate_identifier

from cookbook.domain.ingredients.dtos import IngredientWriteDTO
from cookbook.domain.ingredients.entity import IngredientEntity
from cookbook.extensions.database import Repository


class IngredientRepository(Repository):
    def create(self, ingredient_create_dto: IngredientWriteDTO):
        ingredient = IngredientEntity(uid=generate_identifier())
        self.session.add(ingredient)
        return self.update(ingredient, ingredient_create_dto)
    
    def update(self, ingredient: IngredientEntity, ingredient_create_dto: IngredientWriteDTO):
        for key, value in ingredient_create_dto.dict().items():
            setattr(ingredient, key, value)
        self.session.commit()
        return ingredient

    def get_by_uid(self, ingredient_uid: str):
        ingredient = (
            self.session.query(IngredientEntity)
            .filter(IngredientEntity.uid == ingredient_uid)
            .first()
        )
        if ingredient is None:
            raise HTTPException(404, detail="Ingredient not found")
        return ingredient

    def search(self, name: str = None):
        query = self.session.query(IngredientEntity)
        if name is not None:
            query = query.filter(IngredientEntity.name.icontains(name))
        return query.all()
