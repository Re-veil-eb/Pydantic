from pydantic import BaseModel, model_validator
from typing import Optional
class LoanApplication(BaseModel):
    income: float
    loan_amount: float
    collateral: bool = False

    @model_validator(mode="after")
    def validate_loan(self):
        if self.loan_amount > 5 * self.income and not self.collateral:
            raise ValueError("Loan exceeds 5x income without collateral")
        return self

class JobApplication(BaseModel):
    experience_years: int
    internship_details: Optional[str] = None

    @model_validator(mode="after")
    def validate_experience(self):
        if self.experience_years < 2 and not self.internship_details:
            raise ValueError("Internship details required for <2 years experience")
        return self

class TravelVisa(BaseModel):
    country: str
    passport_validity_months: int

    @model_validator(mode="after")
    def validate_passport(self):
        if self.country == "USA" and self.passport_validity_months < 6:
            raise ValueError("Passport must be valid for at least 6 months for USA")
        return self

class OnlineExam(BaseModel):
    end_time: int
    exam_window: int

    @model_validator(mode="after")
    def validate_exam(self):
        if self.end_time > self.exam_window:
            raise ValueError("Exam must end within exam window")
        return self
