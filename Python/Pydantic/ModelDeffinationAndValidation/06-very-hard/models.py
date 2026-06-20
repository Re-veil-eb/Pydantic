from pydantic import BaseModel, Field, field_validator

# let for example we extracted the info from db and stored in this variable
EXISTING_ACCOUNT_NUMBERS = {"1234567890"}

class BankAccount(BaseModel):
    account_number: str = Field(..., min_length=5)
    balance: float = Field(0.0, ge=0.0)

    @field_validator("account_number")
    @classmethod
    def check_unique_account(cls, value: str) -> str:
        if value in EXISTING_ACCOUNT_NUMBERS:
            raise ValueError("Account number already exists.")
        return value

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Withdrawal exceeds balance.")
        
        self.balance -= amount
