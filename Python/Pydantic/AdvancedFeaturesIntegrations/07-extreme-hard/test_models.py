import pytest
from models import CustomRootList, PositiveIntResponse, SchemaCustomized, CrossLibraryModel

def test_custom_root_list():
    c = CustomRootList([1,2,3])
    assert c.root == [1,2,3]

def test_positive_int_response_valid():
    p = PositiveIntResponse(value=5)
    assert p.value == 5

def test_positive_int_response_invalid():
    with pytest.raises(ValueError):
        PositiveIntResponse(value=-1)

def test_schema_customized():
    s = SchemaCustomized(id=1)
    assert s.id == 1

def test_cross_library_model():
    c = CrossLibraryModel(name="test", data={"k":"v"})
    assert c.data["k"] == "v"
