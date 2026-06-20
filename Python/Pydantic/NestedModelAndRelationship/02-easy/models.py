from pydantic import BaseModel, Field
from typing import List

class Product(BaseModel):
    name: str
    price: float

class Order(BaseModel):
    products: List[Product]

class Address(BaseModel):
    street: str
    city: str
    zip: str = Field(..., regex=r"^\d{5}$")

class Customer(BaseModel):
    name: str
    address: Address
