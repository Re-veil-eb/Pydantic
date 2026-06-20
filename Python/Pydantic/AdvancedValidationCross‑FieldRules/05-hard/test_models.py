import pytest
from models import Flight, ConferenceRoomBooking, InsurancePolicy, Shipment

class TestFlight:
    def test_valid_flight(self):
        f = Flight(departure_airport="DEL", arrival_airport="NYC", route_code="DEL-NYC")
        assert f.route_code == "DEL-NYC"

    def test_invalid_same_airport(self):
        with pytest.raises(ValueError):
            Flight(departure_airport="DEL", arrival_airport="DEL", route_code="DEL-DEL")

class TestConferenceRoomBooking:
    def test_valid_booking(self):
        b = ConferenceRoomBooking(room_capacity=50, attendees=30)
        assert b.attendees <= b.room_capacity

    def test_invalid_booking(self):
        with pytest.raises(ValueError):
            ConferenceRoomBooking(room_capacity=20, attendees=30)

class TestInsurancePolicy:
    def test_valid_health(self):
        p = InsurancePolicy(coverage="health", medical_history="none")
        assert p.coverage == "health"

    def test_invalid_health(self):
        with pytest.raises(ValueError):
            InsurancePolicy(coverage="health")

class TestShipment:
    def test_valid_shipment(self):
        s = Shipment(weight=50, max_allowed_weight=100)
        assert s.weight <= s.max_allowed_weight

    def test_invalid_shipment(self):
        with pytest.raises(ValueError):
            Shipment(weight=150, max_allowed_weight=100)
