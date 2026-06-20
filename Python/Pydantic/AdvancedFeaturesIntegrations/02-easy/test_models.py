import pytest
from models import Product, Session

def test_serialization():
    p = Product(name="Laptop", price=1200)
    assert "Laptop" in p.model_dump_json()

def test_deserialization():
    data = {"name":"Phone","price":800}
    p = Product.model_validate(data)
    assert p.name == "Phone"

def test_schema_generation():
    schema = Product.model_json_schema()
    assert "properties" in schema

def test_default_factory():
    s = Session(id=1)
    assert s.token == "default-token"
