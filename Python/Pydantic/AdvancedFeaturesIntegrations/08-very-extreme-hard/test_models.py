import pytest
from models import SchemaRegistry, DynamicModel, PluginModel, MicroserviceModel, ComplianceModel

def test_schema_registry():
    s = SchemaRegistry(schema_name="user", schema={"id":"int"})
    assert s.schema_name == "user"

def test_dynamic_model():
    d = DynamicModel(field1="abc", field2=10)
    assert d.field1 == "abc"

def test_plugin_model():
    p = PluginModel(plugin_name="auth", config={"enabled":True})
    assert p.config["enabled"]

def test_microservice_model():
    m = MicroserviceModel(service="payment", payload={"amount":100})
    assert m.service == "payment"

def test_compliance_model_valid():
    c = ComplianceModel(pii_data="safe data")
    c.validate_compliance()

def test_compliance_model_invalid():
    with pytest.raises(ValueError):
        ComplianceModel(pii_data="card number 1234").validate_compliance()
