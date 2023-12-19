from uuid import uuid4

from cookbook.domain.groups.dtos import GroupReadDTO, GroupWriteDTO
from cookbook.domain.groups.entity import GroupEntity
from cookbook.extensions.database import Repository


class GroupRepository(Repository):
    def get_by_uid(self, group_uid: str):
        return self.session.query(GroupEntity).filter(GroupEntity.uid == group_uid).first()

    def query(self):
        return self.session.query(GroupEntity)

    def search(self):
        return self.query().all()

    def create(self, group_dto: GroupWriteDTO) -> GroupEntity:
        group = GroupEntity(uid=uuid4().hex)
        self.session.add(group)
        return self.update(group, group_dto)

    def update(self, group: GroupEntity, group_dto: GroupWriteDTO) -> GroupEntity:
        for field, value in group_dto.dict().items():
            setattr(group, field, value)
        self.session.commit()
        return group
