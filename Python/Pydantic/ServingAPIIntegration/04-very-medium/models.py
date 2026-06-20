from fastapi import FastAPI, Request, Depends
from pydantic import BaseModel, model_validator

app = FastAPI()

class Loan(BaseModel):
    income: float
    loan_amount: float
    collateral: bool = False

    @model_validator(mode="after")
    def validate_loan(self):
        if self.loan_amount > 5 * self.income and not self.collateral:
            raise ValueError("Loan exceeds 5x income without collateral")
        return self

@app.post("/loan")
def loan(l: Loan):
    return {"loan": l}

# Dependency injection example
def get_db():
    return {"connection": "db://localhost"}

@app.get("/db")
def db_conn(db=Depends(get_db)):
    return db

# Middleware for error logging
@app.middleware("http")
async def log_errors(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        with open("errors.log", "a") as f:
            f.write(str(e) + "\n")
        raise e
