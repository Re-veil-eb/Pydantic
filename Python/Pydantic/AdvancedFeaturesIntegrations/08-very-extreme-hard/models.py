from pydantic import BaseModel, create_model
from typing import Any, Dict

class SchemaRegistry(BaseModel):
    schema_name: str
    schema: Dict[str, Any]

DynamicModel = create_model("DynamicModel", field1=(str, ...), field2=(int, 0))

class PluginModel(BaseModel):
    plugin_name: str
    config: Dict[str, Any]

class MicroserviceModel(BaseModel):
    service: str
    payload: Dict[str, Any]

class ComplianceModel(BaseModel):
    pii_data: str

    def validate_compliance(self):
        if "card" in self.pii_data.lower():
            raise ValueError("PCI-DSS violation: card data not allowed")
