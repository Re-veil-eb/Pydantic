import pytest
from models import RegistrationForm, AgeCheck, EmailSignup
from datetime import date

class TestRegistrationForm:
    def test_passwords_match(self):
        form = RegistrationForm(password="abc123", confirm_password="abc123")
        assert form.password == form.confirm_password

    def test_passwords_mismatch(self):
        with pytest.raises(ValueError):
            RegistrationForm(password="abc123", confirm_password="xyz")

class TestAgeCheck:
    def test_valid_age(self):
        form = AgeCheck(date_of_birth=date(2000, 1, 1))
        assert isinstance(form, AgeCheck)

    def test_underage(self):
        with pytest.raises(ValueError):
            AgeCheck(date_of_birth=date.today())

class TestEmailSignup:
    def test_valid_email(self):
        form = EmailSignup(email="test@example.com")
        assert "@" in form.email

    def test_invalid_email(self):
        with pytest.raises(ValueError):
            EmailSignup(email="invalid-email")
