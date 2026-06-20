import pytest, hmac, hashlib, json
from datetime import datetime, timedelta
from models import WebhookEvent, SECRET_KEY

class TestWebhookEvent:
    def test_valid_event(self):
        payload = {"event": "payment_success"}
        sig = hmac.new(SECRET_KEY, json.dumps(payload, separators=(",", ":")).encode(), hashlib.sha256).hexdigest()
        event = WebhookEvent(payload=payload, signature=sig, timestamp=datetime.utcnow())
        assert event.payload["event"] == "payment_success"

    def test_invalid_signature(self):
        payload = {"event": "payment_success"}
        with pytest.raises(ValueError):
            WebhookEvent(payload=payload, signature="bad", timestamp=datetime.utcnow())

    def test_expired_event(self):
        payload = {"event": "payment_success"}
        sig = hmac.new(SECRET_KEY, json.dumps(payload, separators=(",", ":")).encode(), hashlib.sha256).hexdigest()
        old_time = datetime.utcnow() - timedelta(minutes=10)
        with pytest.raises(ValueError):
            WebhookEvent(payload=payload, signature=sig, timestamp=old_time)
