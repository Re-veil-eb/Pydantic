from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, Integer, String  # type: ignore
from sqlalchemy.orm import declarative_base  # type: ignore

Base = declarative_base()

class UserORM(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: str

class CeleryPayload(BaseModel):
    task_id: str
    payload: dict

class KafkaMessage(BaseModel):
    topic: str
    key: str
    value: dict

class AirflowConfig(BaseModel):
    dag_id: str
    schedule: str
