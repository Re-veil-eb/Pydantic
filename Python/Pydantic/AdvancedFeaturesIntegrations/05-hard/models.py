from pydantic import BaseModel, ConfigDict
from typing import TypeVar, Generic, List
from decimal import Decimal
from datetime import datetime

T = TypeVar("T")

class NestedGeneric(BaseModel, Generic[T]):
    data: List[T]

class CustomErrorModel(BaseModel):
    value: int

    def validate_value(self):
        if self.value < 0:
            raise ValueError("Value must be positive")

class AdvancedSerialization(BaseModel):
    amount: Decimal
    timestamp: datetime

    model_config = ConfigDict(ser_json_timedelta="iso8601")

class ImmutableModel(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: int
    name: str
