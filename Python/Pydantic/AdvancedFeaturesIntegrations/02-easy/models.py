from pydantic import BaseModel, Field
import json

class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0)

# Serialization
p = Product(name="Laptop", price=1200)
dump_dict = p.model_dump()
dump_json = p.model_dump_json()

# Deserialization
data = {"name": "Phone", "price": 800}
p2 = Product.model_validate(data)

# Schema generation
schema = Product.model_json_schema()

class Session(BaseModel):
    id: int
    token: str = Field(default_factory=lambda: "default-token")
