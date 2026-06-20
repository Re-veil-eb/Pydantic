from pydantic import BaseModel, field_validator
from typing import List

class Factory(BaseModel):
    name: str
    stock: int

class Warehouse(BaseModel):
    name: str
    stock: int

class RetailStore(BaseModel):
    name: str
    stock: int

class SupplyChain(BaseModel):
    factories: List[Factory]
    warehouses: List[Warehouse]
    stores: List[RetailStore]

    @field_validator("warehouses")
    @classmethod
    def validate_warehouses(cls, warehouses):
        for w in warehouses:
            if w.stock < 0:
                raise ValueError("Warehouse stock cannot be negative")
        return warehouses

    @field_validator("stores")
    @classmethod
    def validate_stores(cls, stores, values):
        for s in stores:
            if s.stock < 0:
                raise ValueError("Store stock cannot be negative")
        # Balance check: total warehouse stock == total store stock
        if "warehouses" in values:
            total_wh = sum(w.stock for w in values["warehouses"])
            total_st = sum(s.stock for s in stores)
            if total_wh != total_st:
                raise ValueError("Warehouse and store stock must balance")
        return stores
