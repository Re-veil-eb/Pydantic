from pydantic import BaseModel, model_validator

class SimpleValidationError(BaseModel):
    email: str

    @model_validator(mode="after")
    def validate_email(self):
        if "@" not in self.email or "." not in self.email:
            raise ValueError("Invalid email format")
        return self

class RequiredFieldCheck(BaseModel):
    username: str
    password: str

class DefaultFallback(BaseModel):
    username: str
    nickname: str | None = None

    @model_validator(mode="after")
    def set_default_nickname(self):
        if not self.nickname:
            self.nickname = self.username
        return self
