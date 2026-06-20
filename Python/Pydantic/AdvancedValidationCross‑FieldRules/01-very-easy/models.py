from pydantic import BaseModel, Field, model_validator
from datetime import date

class RegistrationForm(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def check_passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self

class AgeCheck(BaseModel):
    date_of_birth: date

    @model_validator(mode="after")
    def check_age(self):
        age = (date.today() - self.date_of_birth).days // 365
        if age < 18:
            raise ValueError("User must be at least 18 years old")
        return self

class EmailSignup(BaseModel):
    email: str

    @model_validator(mode="after")
    def validate_email(self):
        if "@" not in self.email or "." not in self.email:
            raise ValueError("Invalid email format")
        return self
