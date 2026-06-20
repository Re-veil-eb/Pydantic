from pydantic import BaseModel, Field, ConfigDict, computed_field, field_validator

class ORMUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: str

class AliasedModel(BaseModel):
    external_id: str = Field(alias="externalName")

class ComputedModel(BaseModel):
    first_name: str
    last_name: str

    @computed_field
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

class ValidatedModel(BaseModel):
    password: str

    @field_validator("password")
    def strong_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password too short")
        return v
