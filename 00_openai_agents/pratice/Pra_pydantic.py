from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime
import uuid

class User(BaseModel):
    id: int
    name: str
    age: int= 12
    is_active: bool = True
    email: EmailStr | None = None

# ✅ Correct data
# user = User(id=1, name="Hasan", age=21)
# print(user)

data = {"id": "1", "name": "ALi", "email": "ali@example.com"}
user11 = User.model_validate(data)        # use model_validate in v2
# print(user11)  

# also works with type coercion
# user1 = User(id=23, name="Hasan", age="21")
# print(user1)


# # ❌ Wrong data
# user2 = User(id="23", name="Hasan", age="twenty-one")


class Users(BaseModel):
    id: int
    age: int

# Notice: id is given as string, age is also string
# users = Users(id="100", age="21")

# print(users)
# print(type(users.id), type(users.age))
# print(users.id + 1,",", users.age + 1)  # works fine because of type coercion


class User1(BaseModel):
    id: int
    name: str
    age: Optional[int] = None   # age may or may not be provided
    country: str = "Pakistan"   # default value if not given

# Case 1: Missing optional field
# user1 = User1(id=1, name="Hasan")
# print(user1)

# Case 2: Providing everything
# user2 = User1(id=2, name="Ali", age=25, country="UAE")
# print(user2)

# from pydantic import BaseModel, Field

class User2(BaseModel):
    id: int
    # Field() lets you add rules like gt (greater than), lt (less than), min_length, etc.
    name: str = Field(..., min_length=2)       # name must have at least 2 letters
    age: int = Field(..., gt=0, lt=120)        # age must be >0 and <120
    email: str

# ✅ Correct
# user1 = User2(id=1, name="Hasan", age=21, email="test@example.com")
# print(user1)

# # ❌ Wrong: age is negative
# user2 = User2(id=2, name="Ali", age=-5, email="ali@gmail.com")
# print(user2)


class Address(BaseModel):
    city: str
    country: str

class User3(BaseModel):
    id: int
    name: str
    address: Address   # nested model

# ✅ Correct data
user3 = User3(
    id=1,
    name="Hasan",
    address={"city": "Karachi", "country": "Pakistan"}
)

# print(user3)
# print(user3.address.city)

# for dict output
# print("Dict -->",user.dict())
user_dict = user3.model_dump()   
# print(user_dict)
# print(type(user_dict))

# for json output
user_json = user3.model_dump_json() 
# print(user3.json()) 
# print(user_json)
# print(type(user_json))

# from pydantic import BaseModel, Field

class User4(BaseModel):
    # ... → means required field (must be provided).
    id: int = Field(..., description="Unique user ID")
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(default=18, ge=0, le=120)  # ge = >=, le = <=

# userss = User4(id=1, name="Hasan") # age is optional here by default value 18
# print(userss)

# users1 = User4(id=1, name="Hasan", age=3) # nagative age will raise error
# print(users1)


class User5(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))  # auto-generate unique ID
    created_at: datetime = Field(default_factory=datetime.utcnow)  # auto-set current time
    name: str

# Create user without passing id or created_at
# user = User5(name="Hasan")
# print(user)
# print("id ->",user.id)
# print(user.created_at)


from pydantic import BaseModel, field_validator

class User6(BaseModel):
    name: str
    age: int

    @field_validator("age")
    def age_must_be_even(cls, v):
        if v % 2 != 0:
            raise ValueError("Age must be even")
        return v
# user = User6(name="Hasan", age=22)  # Valid
# print(user)

class Event2(BaseModel):
    id: int
    created_at: datetime = datetime.now()   # BAD: same timestamp reused!

class Event(BaseModel):
    id: int
    created_at: datetime = Field(default_factory=datetime.now)


#generate a print statement for this to explain

# event1 = Event2(id=1)
# event2 = Event(id=2)
# event3 = Event2(id=3)
# event4 = Event(id=4)

# print(event1)
# print(event2)
 
# print(event3)
# print(event4)

from pydantic import  validator

class User7(BaseModel):
    name: str=Field(..., alias="full_name")
    age: int=9

    @validator("name")
    def no_numbers_in_name(cls, v):
        if any(char.isdigit() for char in v):
            raise ValueError("Name cannot contain numbers")
        return v
    
# user = User7(name="Hasan", age=22)  # Valid
# print(user)
# user1 = User7(name="Hasan1", age=22)  # Invalid, raises ValueError


# Incoming data uses "full_name"
data = {"full_name": "Hasan Farid", "age": 21}

use = User7(**data)
# print(use.name)        # "Hasan Farid"
# print(use.model_dump())      # {"name": "Hasan Farid", "age": 21}
# print(use.model_dump(by_alias=True))

from pydantic import BaseModel, field_validator

class Product(BaseModel):
    price: float

    # Validator in "before" mode: runs on raw input before parsing
    @field_validator("price", mode="before")
    def parse_price(cls, v):
        if isinstance(v, str) and v.endswith("$"):
            v = v[:-1]  # Remove currency symbol
        return v

    # Validator in "after" mode: runs on parsed/converted value
    @field_validator("price", mode="after")
    def validate_price(cls, v):
        if v < 0:
            raise ValueError("Price must be a positive value")
        return v

# # Example usage
# product1 = Product(price="100$")
# print(product1)  # Product(price=100.0)

# product2 = Product(price=50)
# print(product2)  # Product(price=50.0)

# This will raise a ValueError because the price is negative
# product3 = Product(price=-10)
