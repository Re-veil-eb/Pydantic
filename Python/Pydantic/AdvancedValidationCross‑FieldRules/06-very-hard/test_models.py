import pytest
from models import LoanApplication, JobApplication, TravelVisa, OnlineExam

class TestLoanApplication:
    def test_valid_loan(self):
        l = LoanApplication(income=1000, loan_amount=4000, collateral=True)
        assert l.collateral is True

    def test_invalid_loan(self):
        with pytest.raises(ValueError):
            LoanApplication(income=1000, loan_amount=6000, collateral=False)

class TestJobApplication:
    def test_valid_experience(self):
        j = JobApplication(experience_years=3)
        assert j.experience_years >= 2

    def test_invalid_experience(self):
        with pytest.raises(ValueError):
            JobApplication(experience_years=1)

class TestTravelVisa:
    def test_valid_passport(self):
        v = TravelVisa(country="USA", passport_validity_months=12)
        assert v.passport_validity_months >= 6

    def test_invalid_passport(self):
        with pytest.raises(ValueError):
            TravelVisa(country="USA", passport_validity_months=3)

class TestOnlineExam:
    def test_valid_exam(self):
        e = OnlineExam(end_time=5, exam_window=10)
        assert e.end_time <= e.exam_window

    def test_invalid_exam(self):
        with pytest.raises(ValueError):
            OnlineExam(end_time=15, exam_window=10)
