from pydantic import BaseModel, model_validator

class TransactionRollback(BaseModel):
    steps: list[str]
    failed_step: str | None = None

    def execute(self):
        if self.failed_step:
            raise ValueError(f"Transaction failed at {self.failed_step}, rolling back")

class MultiErrorAggregation(BaseModel):
    errors: list[str]

    def aggregate(self):
        if self.errors:
            raise ValueError(f"Multiple errors: {', '.join(self.errors)}")

class DeadLetterQueue(BaseModel):
    failed_messages: list[str] = []

    def add(self, message: str):
        self.failed_messages.append(message)

class GracefulShutdown(BaseModel):
    resources: list[str]

    def shutdown(self):
        return f"Closing resources: {', '.join(self.resources)}"
