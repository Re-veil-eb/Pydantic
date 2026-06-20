from pydantic import BaseModel, Field, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")

    username: str = Field(..., title="Username", description="Unique user identifier", example="john_doe")
    age: int = Field(..., ge=0, description="Age must be non-negative")
    email: str = Field(..., example="john@example.com")
