import pytest
from models import NestedGeneric, CustomErrorModel, AdvancedSerialization, ImmutableModel
from decimal import Decimal
from datetime import datetime

def test_nested_generic():
    n = NestedGeneric(data=[1,2,3])
    assert len(n.data) == 3

def test_custom_error_model():
    c = CustomErrorModel(value=5)
    c.validate_value()
    with pytest.raises(ValueError):
        CustomErrorModel(value=-1).validate_value()

def test_advanced_serialization():
    a = AdvancedSerialization(amount=Decimal("10.5"), timestamp=datetime.now())
    assert isinstance(a.amount, Decimal)

def test_immutable_model():
    i = ImmutableModel(id=1, name="test")
    with pytest.raises(TypeError):
        i.name = "new"
