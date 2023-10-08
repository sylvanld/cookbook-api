from fastapi import HTTPException
from cookbook.core.identifiers import generate_identifier

from cookbook.domain.ingredients.entity import IngredientEntity
from cookbook.domain.recipes.dtos import RecipeWriteDTO
from cookbook.domain.recipes.entity import RecipeEntity, RecipeIngredientEntity
from cookbook.extensions.database import Repository


class RecipeRepository(Repository):
    def create(self, recipe_create_dto: RecipeWriteDTO):
        recipe_data = recipe_create_dto.dict()
        recipe_data["uid"] = generate_identifier()
        return RecipeEntity.create(recipe_data)

    def search(self):
        query = self.session.query(RecipeEntity)
        return query.all()

    def get_by_uid(self, recipe_uid: str):
        recipe = (
            self.session.query(RecipeEntity)
            .filter(RecipeEntity.uid == recipe_uid)
            .first()
        )
        if recipe is None:
            raise HTTPException(404, detail="Recipe not found")
        return recipe

    def add_ingredient(
        self,
        recipe: RecipeEntity,
        ingredient: IngredientEntity,
        quantity: float = None,
        unit: str = None,
    ):
        return RecipeIngredientEntity.create(
            {
                "uid": generate_identifier(),
                "recipe_id": recipe.id,
                "ingredient_id": ingredient.id,
                "quantity": quantity,
                "unit": unit,
            }
        )
