import pytest
from models import Transaction

class TestTransaction:
    def test_valid_transaction(self):
        txn = Transaction(amount="100", discount=10, currency="USD")
        assert txn.currency == "USD"

    def test_invalid_currency(self):
        with pytest.raises(ValueError):
            Transaction(amount=100, discount=10, currency="GBP")

    def test_discount_too_high(self):
        with pytest.raises(ValueError):
            Transaction(amount=100, discount=200, currency="USD")
