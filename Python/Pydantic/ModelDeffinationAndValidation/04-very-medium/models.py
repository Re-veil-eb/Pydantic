from pydantic import BaseModel, Field, field_validator
from datetime import datetime
import re

class Payment(BaseModel):
    card_number: str = Field(..., min_length=12, max_length=19)
    expiry_date: str  # format MM/YY
    cvv: str

    # Luhn algorithm for card validation
    @field_validator("card_number")
    @classmethod
    def validate_card_number(cls, value: str) -> str:
        if not value.isdigit():
            raise ValueError("Card number must contain only digits")
        if not cls.luhn_check(value):
            raise ValueError("Invalid credit card number (Luhn check failed)")
        return value

    @classmethod
    def luhn_check(cls, number: str) -> bool:
        total = 0
        reverse_digits = number[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

    # Expiry date validation
    @field_validator("expiry_date")
    @classmethod
    def validate_expiry_date(cls, value: str) -> str:
        pattern = r"^(0[1-9]|1[0-2])\/([0-9]{2})$"
        if not re.match(pattern, value):
            raise ValueError("Expiry date must be in MM/YY format")
        
        month, year = value.split("/")
        exp_date = datetime(int("20" + year), int(month), 1)
        now = datetime.now()
        if exp_date < now.replace(day=1):
            raise ValueError("Card has expired")
        return value

    # CVV validation
    @field_validator("cvv")
    @classmethod
    def validate_cvv(cls, value: str) -> str:
        if not re.match(r"^\d{3}$", value):
            raise ValueError("CVV must be exactly 3 digits")
        return value
