from pydantic import BaseModel, model_validator

class RetryCounter(BaseModel):
    retries: int = 0

    def increment(self):
        self.retries += 1
        if self.retries > 3:
            raise ValueError("Max retries exceeded")

class GracefulTimeout(BaseModel):
    timeout: int

    @model_validator(mode="after")
    def validate_timeout(self):
        if self.timeout > 30:
            raise ValueError("Timeout exceeded threshold")
        return self

class FallbackValue(BaseModel):
    currency: str | None = None

    @model_validator(mode="after")
    def set_default_currency(self):
        if not self.currency:
            self.currency = "USD"
        return self

class ValidationErrorWrapper(BaseModel):
    field: str
    value: str

    @model_validator(mode="after")
    def validate_field(self):
        if not self.value:
            raise ValueError(f"Validation failed for {self.field}")
        return self
