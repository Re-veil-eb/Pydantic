from pydantic import BaseModel, model_validator
from typing import Optional
class Flight(BaseModel):
    departure_airport: str
    arrival_airport: str
    route_code: str

    @model_validator(mode="after")
    def validate_flight(self):
        if self.departure_airport == self.arrival_airport:
            raise ValueError("Departure and arrival airports cannot be the same")
        if self.route_code != f"{self.departure_airport}-{self.arrival_airport}":
            raise ValueError("Route code must match airports")
        return self

class ConferenceRoomBooking(BaseModel):
    room_capacity: int
    attendees: int

    @model_validator(mode="after")
    def validate_capacity(self):
        if self.attendees > self.room_capacity:
            raise ValueError("Attendees exceed room capacity")
        return self

class InsurancePolicy(BaseModel):
    coverage: str
    medical_history: Optional[str] = None

    @model_validator(mode="after")
    def validate_health(self):
        if self.coverage == "health" and not self.medical_history:
            raise ValueError("Medical history required for health coverage")
        return self

class Shipment(BaseModel):
    weight: float
    max_allowed_weight: float

    @model_validator(mode="after")
    def validate_weight(self):
        if self.weight > self.max_allowed_weight:
            raise ValueError("Shipment exceeds max allowed weight")
        return self
