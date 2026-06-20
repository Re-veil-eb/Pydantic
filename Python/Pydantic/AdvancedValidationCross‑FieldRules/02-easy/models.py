from pydantic import BaseModel, Field, model_validator
from datetime import date, datetime

class Booking(BaseModel):
    start_date: date
    end_date: date

    @model_validator(mode="after")
    def validate_dates(self):
        if self.end_date <= self.start_date:
            raise ValueError("End date must be after start date")
        return self

class Event(BaseModel):
    start_time: datetime
    end_time: datetime

    @model_validator(mode="after")
    def validate_times(self):
        if self.end_time <= self.start_time:
            raise ValueError("End time must be after start time")
        return self

class Subscription(BaseModel):
    trial_start: date
    trial_end: date

    @model_validator(mode="after")
    def validate_trial(self):
        if (self.trial_end - self.trial_start).days > 30:
            raise ValueError("Trial period cannot exceed 30 days")
        return self

class Delivery(BaseModel):
    order_date: date
    delivery_date: date

    @model_validator(mode="after")
    def validate_delivery(self):
        if self.delivery_date < self.order_date:
            raise ValueError("Delivery date must be on or after order date")
        return self
