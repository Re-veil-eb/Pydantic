from pydantic import BaseModel, model_validator
from typing import Optional
from datetime import date

class EmployeeCompensation(BaseModel):
    salary: float
    bonus: float

    @model_validator(mode="after")
    def validate_bonus(self):
        if self.bonus > 0.2 * self.salary:
            raise ValueError("Bonus cannot exceed 20% of salary")
        return self

class CourseEnrollment(BaseModel):
    start_date: date
    end_date: date
    semester_end: date

    @model_validator(mode="after")
    def validate_dates(self):
        if self.end_date > self.semester_end:
            raise ValueError("Course end date must be within semester")
        return self

class VehicleRegistration(BaseModel):
    vehicle_type: str
    battery_capacity: Optional[int] = None

    @model_validator(mode="after")
    def validate_electric(self):
        if self.vehicle_type == "electric" and not self.battery_capacity:
            raise ValueError("Battery capacity required for electric vehicles")
        return self

class Membership(BaseModel):
    membership_type: str
    payment_info: Optional[str] = None

    @model_validator(mode="after")
    def validate_premium(self):
        if self.membership_type == "premium" and not self.payment_info:
            raise ValueError("Payment info required for premium membership")
        return self
