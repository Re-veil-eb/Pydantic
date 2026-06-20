from pydantic import BaseModel, Field
import re  
from uuid import uuid4 

class Customer(BaseModel):
    email: str = Field(pattern = r'^[\w\.-]+@[\w]+\.[\w]+$')
    user_id :int = Field(alias = 'uid')
    age: int = Field(ge = 18, le=65)



