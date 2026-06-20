from pydantic import BaseModel, field_validator
from typing import List

class Employee(BaseModel):
    employee_id: str
    role: str

class Company(BaseModel):
    name: str
    employees: List[Employee]

    @field_validator("employees")
    @classmethod
    def validate_employees(cls, employees):
        ids = [e.employee_id for e in employees]
        if len(ids) != len(set(ids)):
            raise ValueError("Employee IDs must be unique")
        if not any(e.role == "CEO" for e in employees):
            raise ValueError("Company must have a CEO")
        return employees
