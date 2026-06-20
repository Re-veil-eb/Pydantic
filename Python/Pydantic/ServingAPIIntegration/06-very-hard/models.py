from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Job(BaseModel):
    job_id: str
    attempts: int = 0

@app.post("/retry")
def retry(j: Job):
    j.attempts += 1
    if j.attempts > 5:
        return {"error": "Max retries exceeded"}
    return {"job": j.job_id, "attempts": j.attempts}

@app.get("/failover")
def failover(primary: bool = True):
    if not primary:
        return {"status": "backup service"}
    return {"status": "primary service"}

@app.get("/metrics")
def metrics():
    return {"errors": {"PaymentError": 2, "AuthError": 1}}
