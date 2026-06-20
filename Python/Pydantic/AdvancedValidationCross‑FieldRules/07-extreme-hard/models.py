from pydantic import BaseModel, model_validator
from typing import List
from datetime import datetime

class Session(BaseModel):
    start_time: datetime
    end_time: datetime

class ConferenceSchedule(BaseModel):
    sessions: List[Session]

    @model_validator(mode="after")
    def validate_sessions(self):
        for i, s1 in enumerate(self.sessions):
            for j, s2 in enumerate(self.sessions):
                if i != j and s1.start_time < s2.end_time and s1.end_time > s2.start_time:
                    raise ValueError("Sessions overlap")
        return self

class ProjectTimeline(BaseModel):
    project_start: datetime
    project_end: datetime
    tasks: List[Session]

    @model_validator(mode="after")
    def validate_tasks(self):
        for t in self.tasks:
            if t.start_time < self.project_start or t.end_time > self.project_end:
                raise ValueError("Task outside project timeline")
        return self

class HospitalShift(BaseModel):
    doctor: str
    start_time: datetime
    end_time: datetime

class ShiftSchedule(BaseModel):
    shifts: List[HospitalShift]

    @model_validator(mode="after")
    def validate_shifts(self):
        for i, s1 in enumerate(self.shifts):
            for j, s2 in enumerate(self.shifts):
                if i != j and s1.doctor == s2.doctor and s1.start_time < s2.end_time and s1.end_time > s2.start_time:
                    raise ValueError("Doctor has overlapping shifts")
        return self
