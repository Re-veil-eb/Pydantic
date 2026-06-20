from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, model_validator

app = FastAPI()

class RegistrationForm(BaseModel):
    username: str
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def validate_passwords(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self

@app.post("/register")
def register(form: RegistrationForm):
    return {"status": "success", "user": form.username}

class Profile(BaseModel):
    username: str
    nickname: str | None = None

    @model_validator(mode="after")
    def set_default(self):
        if not self.nickname:
            self.nickname = self.username
        return self

@app.post("/profile")
def profile(p: Profile):
    return {"profile": p}

@app.get("/search")
def search(query: str):
    return {"query": query}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}
