from pydantic import BaseModel
import time

class ResilientPipeline(BaseModel):
    stages: list[str]

    def run(self):
        results = []
        for stage in self.stages:
            try:
                results.append(f"Stage {stage} succeeded")
            except Exception:
                results.append(f"Stage {stage} failed, continuing")
        return results

class AdaptiveRetry(BaseModel):
    attempts: int = 0

    def retry(self):
        self.attempts += 1
        wait = 2 ** self.attempts
        time.sleep(wait)
        if self.attempts > 5:
            raise ValueError("Max retries exceeded")

class FailoverMechanism(BaseModel):
    primary: bool = True

    def execute(self):
        if not self.primary:
            return "Switched to backup service"
        return "Primary service running"

class ErrorCorrelationID(BaseModel):
    error_id: str
    message: str

    def trace(self):
        return f"[{self.error_id}] {self.message}"
