import pytest
from models import RetryCounter, GracefulTimeout, FallbackValue, ValidationErrorWrapper

class TestRetryCounter:
    def test_increment_valid(self):
        r = RetryCounter()
        r.increment()
        assert r.retries == 1

    def test_increment_exceeds(self):
        r = RetryCounter(retries=3)
        with pytest.raises(ValueError):
            r.increment()

class TestGracefulTimeout:
    def test_valid_timeout(self):
        g = GracefulTimeout(timeout=10)
        assert g.timeout == 10

    def test_invalid_timeout(self):
        with pytest.raises(ValueError):
            GracefulTimeout(timeout=40)

class TestFallbackValue:
    def test_default_currency(self):
        f = FallbackValue()
        assert f.currency == "USD"

    def test_custom_currency(self):
        f = FallbackValue(currency="EUR")
        assert f.currency == "EUR"

class TestValidationErrorWrapper:
    def test_valid_field(self):
        v = ValidationErrorWrapper(field="name", value="John")
        assert v.value == "John"

    def test_invalid_field(self):
        with pytest.raises(ValueError):
            ValidationErrorWrapper(field="name", value="")
