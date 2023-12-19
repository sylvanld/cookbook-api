from uuid import uuid4

from cookbook.domain.groups.entity import GroupEntity
from cookbook.domain.lists.entity import ListRecipeEntity
from cookbook.domain.recipes.entity import RecipeEntity
from cookbook.extensions.database import Repository


class ListRepository(Repository):
    def get_recipes(self, group: GroupEntity):
        return self.session.query(ListRecipeEntity).filter(ListRecipeEntity.group_id == group.id).all()

    def add_recipe(self, group: GroupEntity, recipe: RecipeEntity, diners: int):
        list_recipe = ListRecipeEntity(uid=uuid4().hex, group_id=group.id)
        self.session.add(list_recipe)
        return self.update_recipe(list_recipe, recipe=recipe, diners=diners)

    def update_recipe(self, list_recipe: ListRecipeEntity, recipe: RecipeEntity, diners: int):
        list_recipe.recipe = recipe
        list_recipe.diners = diners
        self.session.commit()
        return list_recipe
