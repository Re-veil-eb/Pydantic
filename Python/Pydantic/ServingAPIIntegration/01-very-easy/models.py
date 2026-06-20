from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

class User(BaseModel):
    username: str
    email: str

@app.post("/user")
def create_user(user: User):
    return {"user": user}

@app.post("/echo")
def echo(payload: dict):
    return {"echo": payload}
