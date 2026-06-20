from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, model_validator
from typing import List

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float

class Order(BaseModel):
    products: List[Product]

@app.post("/order")
def order(o: Order):
    return {"order_total": sum(p.price for p in o.products)}

class Discount(BaseModel):
    percentage: float | None = None
    amount: float | None = None

    @model_validator(mode="after")
    def validate_discount(self):
        if self.percentage and self.amount:
            raise ValueError("Only one discount allowed")
        return self

@app.post("/discount")
def discount(d: Discount):
    return {"discount": d}

@app.exception_handler(ValueError)
def custom_error_handler(_, exc: ValueError):
    return HTTPException(status_code=400, detail={"code": 400, "message": str(exc)})

class Invoice(BaseModel):
    total: float
    items: List[float]

    @model_validator(mode="after")
    def validate_total(self):
        if sum(self.items) != self.total:
            raise ValueError("Invoice total mismatch")
        return self

@app.post("/invoice", response_model=Invoice)
def invoice(i: Invoice):
    return i
