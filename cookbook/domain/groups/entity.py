from sqlalchemy import Column, Integer, String

from cookbook.extensions.database import Entity


class GroupEntity(Entity):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    uid = Column(String(32), unique=True)
    name = Column(String(25), nullable=False)
