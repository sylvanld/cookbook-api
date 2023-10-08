from sqlalchemy import Column, Integer, String

from cookbook.extensions.database import Entity


class IngredientEntity(Entity):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True)
    uid = Column(String(32), unique=True, nullable=False)
    name = Column(String(30), unique=True, nullable=False)
    unit = Column(String(30), nullable=True)
    shelve = Column(String(30), nullable=False)
