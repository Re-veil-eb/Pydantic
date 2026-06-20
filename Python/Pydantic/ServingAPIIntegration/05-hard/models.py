from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Transaction(BaseModel):
    steps: list[str]
    fail: bool = False

@app.post("/transaction")
def transaction(t: Transaction):
    if t.fail:
        raise HTTPException(status_code=400, detail="Transaction failed, rolled back")
    return {"status": "success"}

class Batch(BaseModel):
    items: list[str]

@app.post("/batch")
def batch(b: Batch):
    processed = [i for i in b.items if "fail" not in i]
    failed = [i for i in b.items if "fail" in i]
    return {"processed": processed, "failed": failed}

class DLQ(BaseModel):
    failed: list[str]

@app.post("/dlq")
def dlq(d: DLQ):
    return {"dlq": d.failed}

@app.on_event("shutdown")
def shutdown_event():
    print("Closing DB connections...")
