from fastapi import FastAPI, HTTPException
import random

app = FastAPI()

@app.exception_handler(Exception)
def global_error_handler(_, exc: Exception):
    return HTTPException(status_code=500, detail=f"Global handler caught: {str(exc)}")

@app.get("/chaos")
def chaos():
    if random.choice([True, False]):
        raise HTTPException(status_code=500, detail="Injected chaos failure")
    return {"status": "stable"}

@app.get("/propagate")
def propagate(error: str, services: list[str]):
    return {s: f"Error propagated: {error}" for s in services}

@app.get("/compliance")
def compliance():
    return {"logs": ["error1", "error2"], "immutable": True}

@app.get("/observability")
def observability():
    return {"metrics": {"errors": 10}, "tracing": True, "logs": ["trace1","trace2"]}
