import hmac
import hashlib
import json
from datetime import datetime, timedelta
from pydantic import BaseModel, Field, field_validator

SECRET_KEY = b"supersecretkey"  # In production, load from env variable

class WebhookEvent(BaseModel):
    payload: dict
    signature: str
    timestamp: datetime = Field(...)

    @field_validator("payload")
    @classmethod
    def validate_payload(cls, value):
        # Ensure payload is JSON-serializable
        try:
            json.dumps(value)
        except Exception:
            raise ValueError("Payload must be valid JSON")
        return value

    @field_validator("signature")
    @classmethod
    def validate_signature(cls, value, values):
        payload = values.get("payload")
        if payload is None:
            raise ValueError("Payload must be validated first")

        # Compute HMAC SHA256
        computed_sig = hmac.new(
            SECRET_KEY,
            json.dumps(payload, separators=(",", ":")).encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

        if not hmac.compare_digest(computed_sig, value):
            raise ValueError("Invalid signature")
        return value

    @field_validator("timestamp")
    @classmethod
    def validate_timestamp(cls, value):
        now = datetime.utcnow()
        if value < now - timedelta(minutes=5):
            raise ValueError("Event timestamp too old")
        return value
