from pydantic.dataclasses import dataclass
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime



@dataclass
class User:
    id: int
    username: str
    first_name: str
    last_name: str
    age: int
    created_at: datetime


class UpdateUserSchema(BaseModel):
    id: Optional[int]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    age: Optional[int]
    created_at: Optional[datetime]


@dataclass
class UserList:
    count: int
    users: List[User]




# class UserSchema(BaseModel):
#     id: int
#     username: str
#     first_name: str
#     last_name: str
#     age: int
#     created_at: datetime

#     class Config:
#         schema_extra = {
#             'example':
#             {
#                 'id': 111,
#                 'username': 'username_111',
#                 'first_name': 'first_name_111',
#                 'last_name': 'last_name_111',
#                 'age': 111,
#                 'created_at': datetime.now(),
#             }
#         }