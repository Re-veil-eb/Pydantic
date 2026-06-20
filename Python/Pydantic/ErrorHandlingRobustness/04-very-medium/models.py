from pydantic import BaseModel, model_validator
import json

class APIResponseValidator(BaseModel):
    response: dict

    @model_validator(mode="after")
    def validate_response(self):
        required_keys = ["status", "data"]
        for key in required_keys:
            if key not in self.response:
                raise ValueError(f"Missing key: {key}")
        return self

class CircuitBreaker(BaseModel):
    failures: int = 0

    def record_failure(self):
        self.failures += 1
        if self.failures >= 5:
            raise ValueError("Circuit breaker triggered")

class ErrorLogging(BaseModel):
    error_message: str

    def log_error(self, file="errors.log"):
        with open(file, "a") as f:
            f.write(self.error_message + "\n")

class StructuredError(BaseModel):
    code: int
    message: str

    def to_json(self):
        return json.dumps({"code": self.code, "message": self.message})
