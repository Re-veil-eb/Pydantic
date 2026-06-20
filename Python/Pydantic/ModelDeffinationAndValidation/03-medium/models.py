from typing import Union
from pydantic import Field, BaseModel, field_validator

class Transaction(BaseModel):
    amount: Union[float, str] = Field(ge = 0)
    discount: float = Field(ge = 0, le = 100) #this ensure the amount must be greater than or equal to discount
    currency: str

    @field_validator('currency')
    @classmethod
    def validate_currency(cls, value):
        value = value.upper()
        if value not in ('USD', 'EUR', 'INR'):
            raise ValueError("currency must be in USD, EUR, INR")
        return value

    
    

