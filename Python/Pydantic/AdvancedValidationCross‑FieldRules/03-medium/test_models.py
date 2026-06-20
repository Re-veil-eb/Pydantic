import pytest
from models import Discount, Payment, ProfileUpdate, Reservation

class TestDiscount:
    def test_valid_percentage(self):
        d = Discount(percentage=10)
        assert d.percentage == 10

    def test_invalid_both_set(self):
        with pytest.raises(ValueError):
            Discount(percentage=10, amount=100)

class TestPayment:
    def test_valid_card(self):
        p = Payment(card_number="1234", expiry_date="12/30", cvv="123")
        assert p.cvv == "123"

    def test_missing_card_info(self):
        with pytest.raises(ValueError):
            Payment(card_number="1234")

class TestProfileUpdate:
    def test_email_update_resets_verification(self):
        p = ProfileUpdate(email="new@example.com")
        assert p.email_verified is False

class TestReservation:
    def test_valid_reservation(self):
        r = Reservation(guest_count=5, max_capacity=10)
        assert r.guest_count <= r.max_capacity

    def test_invalid_reservation(self):
        with pytest.raises(ValueError):
            Reservation(guest_count=15, max_capacity=10)
