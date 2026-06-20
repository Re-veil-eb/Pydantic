from fastapi import FastAPI, Request
from pydantic import BaseModel
import uuid

app = FastAPI()

class Pipeline(BaseModel):
    stages: list[str]

@app.post("/pipeline")
def pipeline(p: Pipeline):
    results = []
    for stage in p.stages:
        try:
            results.append(f"{stage} succeeded")
        except Exception:
            results.append(f"{stage} failed, continuing")
    return {"results": results}

@app.middleware("http")
async def correlation_id_middleware(request: Request, call_next):
    correlation_id = str(uuid.uuid4())
    response = await call_next(request)
    response.headers["X-Correlation-ID"] = correlation_id
    return response

class AuditTrail(BaseModel):
    logs: list[str]

@app.post("/audit")
def audit(a: AuditTrail):
    return {"audit": a.logs}
