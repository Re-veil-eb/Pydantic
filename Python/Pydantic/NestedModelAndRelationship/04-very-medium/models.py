from pydantic import BaseModel, field_validator
from typing import List

class Student(BaseModel):
    roll_number: int
    name: str

class Classroom(BaseModel):
    students: List[Student]

    @field_validator("students")
    @classmethod
    def validate_students(cls, students):
        if len(students) > 30:
            raise ValueError("Classroom cannot exceed 30 students")
        roll_numbers = [s.roll_number for s in students]
        if len(roll_numbers) != len(set(roll_numbers)):
            raise ValueError("Duplicate roll numbers in classroom")
        return students

class School(BaseModel):
    name: str
    classrooms: List[Classroom]
