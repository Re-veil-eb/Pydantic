import pytest
from models import EmployeeCompensation, CourseEnrollment, VehicleRegistration, Membership
from datetime import date, timedelta

class TestEmployeeCompensation:
    def test_valid_bonus(self):
        e = EmployeeCompensation(salary=1000, bonus=200)
        assert e.bonus <= 0.2 * e.salary

    def test_invalid_bonus(self):
        with pytest.raises(ValueError):
            EmployeeCompensation(salary=1000, bonus=300)

class TestCourseEnrollment:
    def test_valid_course(self):
        c = CourseEnrollment(start_date=date.today(), end_date=date.today()+timedelta(days=30), semester_end=date.today()+timedelta(days=60))
        assert c.end_date <= c.semester_end

    def test_invalid_course(self):
        with pytest.raises(ValueError):
            CourseEnrollment(start_date=date.today(), end_date=date.today()+timedelta(days=90), semester_end=date.today()+timedelta(days=60))

class TestVehicleRegistration:
    def test_valid_electric(self):
        v = VehicleRegistration(vehicle_type="electric", battery_capacity=100)
        assert v.battery_capacity == 100

    def test_invalid_electric(self):
        with pytest.raises(ValueError):
            VehicleRegistration(vehicle_type="electric")

class TestMembership:
    def test_valid_premium(self):
        m = Membership(membership_type="premium", payment_info="card123")
        assert m.payment_info is not None

    def test_invalid_premium(self):
        with pytest.raises(ValueError):
            Membership(membership_type="premium")
