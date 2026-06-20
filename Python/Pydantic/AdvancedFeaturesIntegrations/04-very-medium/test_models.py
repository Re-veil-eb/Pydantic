import pytest
from models import ORMUser, AliasedModel, ComputedModel, ValidatedModel

def test_orm_user():
    u = ORMUser(id=1, username="john", email="john@example.com")
    assert u.username == "john"

def test_alias_model():
    a = AliasedModel(externalName="ext123")
    assert a.external_id == "ext123"

def test_computed_field():
    c = ComputedModel(first_name="John", last_name="Doe")
    assert c.full_name == "John Doe"

def test_validated_model_valid():
    v = ValidatedModel(password="strongpass")
    assert v.password == "strongpass"

def test_validated_model_invalid():
    with pytest.raises(ValueError):
        ValidatedModel(password="short")
