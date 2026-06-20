from pydantic import BaseModel, model_validator
from typing import Optional

class Discount(BaseModel):
    percentage: Optional[float] = None
    amount: Optional[float] = None

    @model_validator(mode="after")
    def validate_discount(self):
        if self.percentage and self.amount:
            raise ValueError("Only one discount type allowed")
        return self

class Payment(BaseModel):
    card_number: Optional[str]
    expiry_date: Optional[str]
    cvv: Optional[str]

    @model_validator(mode="after")
    def validate_card_info(self):
        if self.card_number and (not self.expiry_date or not self.cvv):
            raise ValueError("Expiry date and CVV required with card number")
        return self

class ProfileUpdate(BaseModel):
    email: str
    email_verified: bool = True

    @model_validator(mode="after")
    def reset_verification(self):
        if not self.email_verified:
            return self
        # If email changes, reset verification
        self.email_verified = False
        return self

class Reservation(BaseModel):
    guest_count: int
    max_capacity: int

    @model_validator(mode="after")
    def validate_capacity(self):
        if self.guest_count > self.max_capacity:
            raise ValueError("Guest count exceeds capacity")
        return self
