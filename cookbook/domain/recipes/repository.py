from fastapi import HTTPException

from cookbook.core.identifiers import generate_identifier
from cookbook.domain.ingredients.entity import IngredientEntity
from cookbook.domain.recipes.dtos import RecipeWriteDTO
from cookbook.domain.recipes.entity import RecipeEntity, RecipeIngredientEntity
from cookbook.domain.recipes.query import RecipeQuery
from cookbook.extensions.database import Repository


class RecipeRepository(Repository):
    def create(self, recipe_create_dto: RecipeWriteDTO):
        recipe = RecipeEntity(uid=generate_identifier())
        self.session.add(recipe)
        return self.update(recipe, recipe_create_dto)

    def update(self, recipe: RecipeEntity, recipe_write_dto: RecipeWriteDTO):
        for key, value in recipe_write_dto.dict().items():
            setattr(recipe, key, value)
        self.session.commit()
        return recipe

    def delete(self, recipe: RecipeEntity):
        self.session.delete(recipe)
        self.session.commit()

    def search(self, recipe_query: RecipeQuery):
        query = self.session.query(RecipeEntity)
        if recipe_query.name:
            query = query.filter(RecipeEntity.name.icontains(recipe_query.name))
        return query.limit(50).all()

    def get_by_uid(self, recipe_uid: str):
        recipe = self.session.query(RecipeEntity).filter(RecipeEntity.uid == recipe_uid).first()
        if recipe is None:
            raise HTTPException(404, detail="Recipe not found")
        return recipe

    def get_ingredient(self, recipe_ingredient_uid: str) -> RecipeIngredientEntity:
        ingredient = (
            self.session.query(RecipeIngredientEntity)
            .filter(RecipeIngredientEntity.uid == recipe_ingredient_uid)
            .first()
        )
        if ingredient is None:
            raise HTTPException(404, detail="Ingredient not found")
        return ingredient

    def add_ingredient(
        self,
        recipe: RecipeEntity,
        ingredient: IngredientEntity,
        quantity: float = None,
        unit: str = None,
    ):
        recipe_ingredient = RecipeIngredientEntity(
            uid=generate_identifier(),
            recipe_id=recipe.id,
            ingredient_id=ingredient.id,
            quantity=quantity,
            unit=unit,
        )
        self.session.add(recipe_ingredient)
        self.session.commit()
        return recipe_ingredient

    def update_ingredient(
        self,
        recipe_ingredient: RecipeIngredientEntity,
        quantity: float = None,
        unit: str = None,
        ingredient: IngredientEntity = None,
    ):
        recipe_ingredient.quantity = quantity
        recipe_ingredient.unit = unit
        recipe_ingredient.ingredient = ingredient
        self.session.commit()
        return recipe_ingredient

    def delete_ingredient(self, ingredient: RecipeIngredientEntity):
        self.session.delete(ingredient)
        self.session.commit()
