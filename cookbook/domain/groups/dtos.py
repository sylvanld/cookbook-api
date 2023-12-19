from pydantic import BaseModel


class GroupWriteDTO(BaseModel):
    name: str


class GroupReadDTO(BaseModel):
    uid: str
    name: str
