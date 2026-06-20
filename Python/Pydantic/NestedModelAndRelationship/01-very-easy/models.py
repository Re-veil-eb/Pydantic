from pydantic import BaseModel, Field

class Profile(BaseModel):
    bio: str
    website: str

class User(BaseModel):
    username: str
    profile: Profile

class Category(BaseModel):
    name: str

class Product(BaseModel):
    name: str
    category: Category
