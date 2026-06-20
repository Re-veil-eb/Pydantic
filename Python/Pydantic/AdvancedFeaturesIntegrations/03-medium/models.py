from pydantic import BaseModel, EmailStr, HttpUrl, Field
from typing import TypeVar, Generic, List, Annotated

T = TypeVar("T")

class PaginatedResponse(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    size: int

class CustomTypes(BaseModel):
    username: Annotated[str, Field(min_length=3, max_length=20)]
    age: Annotated[int, Field(gt=0, lt=120)]
    tags: Annotated[List[str], Field(min_length=1)]
    email: EmailStr
    website: HttpUrl
