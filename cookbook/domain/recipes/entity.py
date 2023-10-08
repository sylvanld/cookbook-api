from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from cookbook.extensions.database import Entity


class RecipeEntity(Entity):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)

    uid = Column(String(20), unique=True, nullable=False)
    name = Column(String(32), unique=True, nullable=False)
    diners = Column(Integer, nullable=False)
    is_public = Column(Boolean, default=False, nullable=False)

    ingredients = relationship("RecipeIngredientEntity")


class RecipeIngredientEntity(Entity):
    __tablename__ = "recipe_ingredients"

    id = Column(Integer, primary_key=True)
    recipe_id = Column(ForeignKey("recipes.id"), nullable=False)
    ingredient_id = Column(ForeignKey("ingredients.id"), nullable=False)

    uid = Column(String(20), unique=True, nullable=False)
    quantity = Column(Float, nullable=True)
    unit = Column(String(10), nullable=True)

    ingredient = relationship("IngredientEntity")
