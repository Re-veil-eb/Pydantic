from pydantic import BaseModel, model_validator

class PaymentError(Exception):
    pass

class Payment(BaseModel):
    amount: float

    @model_validator(mode="after")
    def validate_amount(self):
        if self.amount <= 0:
            raise PaymentError("Invalid payment amount")
        return self

class WebhookRetry(BaseModel):
    retries: int = 0

    def attempt(self):
        self.retries += 1
        if self.retries > 3:
            raise ValueError("Webhook validation failed after 3 retries")

class DatabaseConnection(BaseModel):
    connection_string: str

    @model_validator(mode="after")
    def validate_connection(self):
        if not self.connection_string.startswith("db://"):
            raise ValueError("Invalid database connection string")
        return self

class GracefulDegradation(BaseModel):
    service_available: bool = True

    def process(self):
        if not self.service_available:
            return "Service degraded, continuing with limited functionality"
        return "Service running normally"
