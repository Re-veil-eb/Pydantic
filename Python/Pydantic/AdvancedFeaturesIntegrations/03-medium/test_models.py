import pytest
from models import PaginatedResponse, CustomTypes

def test_paginated_response():
    p = PaginatedResponse(items=[1,2,3], total=3, page=1, size=3)
    assert p.total == 3

def test_custom_types_valid():
    c = CustomTypes(username="john123", age=25, tags=["tag1"], email="john@example.com", website="http://example.com")
    assert c.username == "john123"

def test_custom_types_invalid_age():
    with pytest.raises(ValueError):
        CustomTypes(username="john123", age=-1, tags=["tag1"], email="john@example.com", website="http://example.com")
