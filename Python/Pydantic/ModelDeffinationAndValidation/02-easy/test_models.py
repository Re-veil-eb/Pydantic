import pytest
from models import Customer

class TestCustomer:
    def test_valid_customer(self):
        customer = Customer(uid=1, email="test@example.com", age=25)
        assert customer.user_id == 1

    def test_invalid_email(self):
        with pytest.raises(ValueError):
            Customer(uid=1, email="invalid-email", age=25)

    def test_invalid_age(self):
        with pytest.raises(ValueError):
            Customer(uid=1, email="test@example.com", age=70)
