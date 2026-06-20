from pydantic import BaseModel
import random

class GlobalErrorHandler(BaseModel):
    service: str

    def handle(self, error: str):
        return f"Global handler caught error in {self.service}: {error}"

class ChaosTesting(BaseModel):
    def inject_failure(self):
        if random.choice([True, False]):
            raise ValueError("Injected random failure")

class SelfHealingSystem(BaseModel):
    service_status: str = "healthy"

    def heal(self):
        if self.service_status == "failed":
            self.service_status = "recovered"
        return self.service_status

class AuditTrail(BaseModel):
    logs: list[str] = []

    def record(self, error: str):
        self.logs.append(error)

class CrossServiceErrorPropagation(BaseModel):
    error: str
    services: list[str]

    def propagate(self):
        return [f"{s} received error: {self.error}" for s in self.services]
