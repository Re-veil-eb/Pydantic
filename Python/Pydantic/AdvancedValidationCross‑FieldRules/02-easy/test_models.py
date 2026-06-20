import pytest
from models import Booking, Event, Subscription, Delivery
from datetime import date, datetime, timedelta

class TestBooking:
    def test_valid_booking(self):
        b = Booking(start_date=date.today(), end_date=date.today() + timedelta(days=1))
        assert b.end_date > b.start_date

    def test_invalid_booking(self):
        with pytest.raises(ValueError):
            Booking(start_date=date.today(), end_date=date.today())

class TestEvent:
    def test_valid_event(self):
        e = Event(start_time=datetime(2026, 6, 20, 10), end_time=datetime(2026, 6, 20, 12))
        assert e.end_time > e.start_time

    def test_invalid_event(self):
        with pytest.raises(ValueError):
            Event(start_time=datetime(2026, 6, 20, 12), end_time=datetime(2026, 6, 20, 10))

class TestSubscription:
    def test_valid_trial(self):
        s = Subscription(trial_start=date.today(), trial_end=date.today() + timedelta(days=10))
        assert (s.trial_end - s.trial_start).days <= 30

    def test_invalid_trial(self):
        with pytest.raises(ValueError):
            Subscription(trial_start=date.today(), trial_end=date.today() + timedelta(days=40))

class TestDelivery:
    def test_valid_delivery(self):
        d = Delivery(order_date=date.today(), delivery_date=date.today() + timedelta(days=2))
        assert d.delivery_date >= d.order_date

    def test_invalid_delivery(self):
        with pytest.raises(ValueError):
            Delivery(order_date=date.today(), delivery_date=date.today() - timedelta(days=1))
