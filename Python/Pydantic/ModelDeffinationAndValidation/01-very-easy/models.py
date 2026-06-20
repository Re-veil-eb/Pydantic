from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class User(BaseModel):
    username: str = Field(min_length = 3, max_length = 50)
    email: EmailStr
    age: int =  Field(gt = 0, lt = 120)

class Product(BaseModel):
    price: float = Field(ge = 0)
    created_at: datetime = Field(default_factory = datetime.now)


