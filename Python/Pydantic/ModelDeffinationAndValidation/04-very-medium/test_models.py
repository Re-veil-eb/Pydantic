import pytest
from models import Payment

class TestPayment:
    def test_valid_payment(self):
        payment = Payment(card_number="4111111111111111", expiry_date="12/30", cvv="123")
        assert payment.cvv == "123"

    def test_invalid_card_number(self):
        with pytest.raises(ValueError):
            Payment(card_number="123456", expiry_date="12/30", cvv="123")

    def test_expired_card(self):
        with pytest.raises(ValueError):
            Payment(card_number="4111111111111111", expiry_date="01/20", cvv="123")

    def test_invalid_cvv(self):
        with pytest.raises(ValueError):
            Payment(card_number="4111111111111111", expiry_date="12/30", cvv="12")
