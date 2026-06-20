import pytest
from models import Payment, PaymentError, WebhookRetry, DatabaseConnection, GracefulDegradation

class TestPayment:
    def test_valid_payment(self):
        p = Payment(amount=100)
        assert p.amount == 100

    def test_invalid_payment(self):
        with pytest.raises(PaymentError):
            Payment(amount=0)

class TestWebhookRetry:
    def test_valid_attempts(self):
        w = WebhookRetry()
        w.attempt()
        assert w.retries == 1

    def test_exceed_attempts(self):
        w = WebhookRetry(retries=3)
        with pytest.raises(ValueError):
            w.attempt()

class TestDatabaseConnection:
    def test_valid_connection(self):
        d = DatabaseConnection(connection_string="db://localhost")
        assert d.connection_string.startswith("db://")

    def test_invalid_connection(self):
        with pytest.raises(ValueError):
            DatabaseConnection(connection_string="http://localhost")

class TestGracefulDegradation:
    def test_service_available(self):
        g = GracefulDegradation(service_available=True)
        assert g.process() == "Service running normally"

    def test_service_unavailable(self):
        g = GracefulDegradation(service_available=False)
        assert "degraded" in g.process()
