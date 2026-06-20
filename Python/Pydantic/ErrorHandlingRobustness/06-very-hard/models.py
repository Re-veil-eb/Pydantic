from pydantic import BaseModel

class DistributedRetry(BaseModel):
    job_id: str
    attempts: int = 0

    def retry(self):
        self.attempts += 1
        if self.attempts > 5:
            raise ValueError("Job failed across workers")

class PartialSuccess(BaseModel):
    processed: list[str]
    failed: list[str]

    def summary(self):
        return {"processed": self.processed, "failed": self.failed}

class CustomExceptionHierarchy(Exception):
    pass

class PaymentError(CustomExceptionHierarchy):
    pass

class AuthError(CustomExceptionHierarchy):
    pass

class ErrorMetrics(BaseModel):
    error_counts: dict[str, int] = {}

    def record(self, error_type: str):
        self.error_counts[error_type] = self.error_counts.get(error_type, 0) + 1
