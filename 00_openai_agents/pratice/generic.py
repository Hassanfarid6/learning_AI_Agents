from pydantic import BaseModel
from typing import Generic, TypeVar, List, Dict

T = TypeVar("T")

class Response(BaseModel, Generic[T]):
    data: T
    success: bool

# Example 1: Integer data
res_int = Response[str](data="123", success=True)
# print(res_int)  # Response(data=123, success=True)

# # Example 2: String data
# res_str = Response[str](data="Operation completed", success=True)
# print(res_str)  # Response(data='Operation completed', success=True)

# # Example 3: List of integers
# res_list = Response[List[int]](data=[1, 2, 3, 4], success=True)
# print(res_list)  # Response(data=[1, 2, 3, 4], success=True)

# # Example 4: Dictionary data
# res_dict = Response[Dict[str, str]](data={"key": "value"}, success=False)
# print(res_dict)  # Response(data={'key': 'value'}, success=False)

# # Example 5: Nested Response
# nested_res = Response[Response[int]](data=Response[int](data=42, success=True), success=True)
# print(nested_res)
# # Response(data=Response(data=42, success=True), success=True)


# Enum

from enum import Enum
from pydantic import BaseModel

class Role(str, Enum):
    admin = "admin"
    editor = "editor"
    viewer = "viewer"

class User(BaseModel):
    id: int
    name: str
    role: Role   # must be one of Role

# ✅ Correct
user1 = User(id=1, name="Hasan", role="admin")
# print(user1)

# ❌ Wrong
# user2 = User(id=2, name="Ali", role="superuser")

# Advance Pydantic
# Ye ek fake ORM class hai (database row jesi)
class UserORM:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

class User(BaseModel):
    id: int
    name: str
    age: int

    class Config:
        from_attributes = True   # 👈 ORM mode enable ho gaya (Pydantic v2 mein)

# ORM object banate hain
orm_user = UserORM(id=1, name="Hasan", age=21)

# Pydantic model ke through parse karte hain
user = User.model_validate(orm_user)
print(user.model_dump())


# class User(BaseModel):
#     id: int
#     name: str

#     class Config:
#         # agar extra field aaye to error throw ho
#         extra = "forbid"

#         # har cheez ko strict type me check kare
#         strict = True

