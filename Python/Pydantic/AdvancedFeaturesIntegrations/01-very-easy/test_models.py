import pytest
from models import User

def test_valid_user():
    u = User(username="john", age=30, email="john@example.com")
    assert u.username == "john"

def test_invalid_age():
    with pytest.raises(ValueError):
        User(username="john", age=-5, email="john@example.com")

def test_extra_field_forbidden():
    with pytest.raises(ValueError):
        User(username="john", age=25, email="john@example.com", extra="oops")
