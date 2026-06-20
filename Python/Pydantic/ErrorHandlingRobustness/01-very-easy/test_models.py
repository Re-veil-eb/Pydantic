import pytest
from models import SimpleValidationError, RequiredFieldCheck, DefaultFallback

class TestSimpleValidationError:
    def test_valid_email(self):
        s = SimpleValidationError(email="test@example.com")
        assert "@" in s.email

    def test_invalid_email(self):
        with pytest.raises(ValueError):
            SimpleValidationError(email="invalid")

class TestRequiredFieldCheck:
    def test_required_fields(self):
        r = RequiredFieldCheck(username="user", password="pass")
        assert r.username == "user"

class TestDefaultFallback:
    def test_default_nickname(self):
        d = DefaultFallback(username="john")
        assert d.nickname == "john"

    def test_custom_nickname(self):
        d = DefaultFallback(username="john", nickname="jdoe")
        assert d.nickname == "jdoe"
