from typing import List
from uuid import uuid4

from fastapi import APIRouter

from cookbook.domain.groups.dtos import GroupReadDTO, GroupWriteDTO
from cookbook.domain.groups.repository import GroupRepository

router = APIRouter()
group_repository = GroupRepository()


@router.get("/groups", response_model=List[GroupReadDTO])
async def search_groups():
    return group_repository.search()


@router.post("/groups", response_model=GroupReadDTO)
async def create_group(group_dto: GroupWriteDTO):
    return group_repository.create(group_dto)
