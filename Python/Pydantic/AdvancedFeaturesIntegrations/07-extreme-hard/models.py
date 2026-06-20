from pydantic import BaseModel, RootModel, Field
from typing import List, Dict, TypeVar, Generic

class CustomRootList(RootModel[List[int]]):
    pass

T = TypeVar("T")

class PositiveIntResponse(BaseModel, Generic[T]):
    value: T = Field(..., gt=0)

class SchemaCustomized(BaseModel):
    id: int = Field(..., description="Unique identifier", examples=[1,2,3], deprecated=False)

class CrossLibraryModel(BaseModel):
    name: str
    data: Dict[str, str]
