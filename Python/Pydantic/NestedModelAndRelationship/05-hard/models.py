from pydantic import BaseModel, field_validator
from typing import List

class LineItem(BaseModel):
    description: str
    total: float

class Invoice(BaseModel):
    invoice_total: float
    line_items: List[LineItem]

    @field_validator("line_items")
    @classmethod
    def validate_invoice(cls, items, values):
        expected_total = sum(item.total for item in items)
        if "invoice_total" in values and values["invoice_total"] != expected_total:
            raise ValueError("Invoice total does not match sum of line items")
        return items
