from typing import Optional
from pydantic import BaseModel


class BaseModelModify(BaseModel):
    id: Optional[int]


class Equipment(BaseModelModify):
    equipment: str


class Resource(BaseModelModify):
    resource: str


class Post(BaseModelModify):
    position: str


class Firm(BaseModelModify):
    equipment_id: int
    resource_id: int
    title: str
    phone: str
    city: str


class Staff(BaseModelModify):
    firm_id: int
    post_id: int
    name: str
    surname: str
    patronymic: str
    date_of_birth: str
