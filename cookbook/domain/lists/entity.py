from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from cookbook.extensions.database import Entity


class ListRecipeEntity(Entity):
    __tablename__ = "list_recipes"

    id = Column(Integer, primary_key=True)
    uid = Column(String(32), unique=True, nullable=False)
    diners = Column(Integer, nullable=False)

    group_id = Column(ForeignKey("groups.id"), nullable=False)
    recipe_id = Column(ForeignKey("recipes.id"), nullable=False)

    recipe = relationship("RecipeEntity", cascade="all,delete")
