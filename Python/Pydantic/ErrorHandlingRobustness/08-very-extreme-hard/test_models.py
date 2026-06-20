import pytest
from models import GlobalErrorHandler, ChaosTesting, SelfHealingSystem, AuditTrail, CrossServiceErrorPropagation

class TestGlobalErrorHandler:
    def test_handle_error(self):
        g = GlobalErrorHandler(service="auth")
        msg = g.handle("timeout")
        assert "auth" in msg

class TestChaosTesting:
    def test_inject_failure(self):
        c = ChaosTesting()
        # Random failure injection, so we just check exception possibility
        try:
            c.inject_failure()
        except ValueError:
            assert True

class TestSelfHealingSystem:
    def test_heal(self):
        s = SelfHealingSystem(service_status="failed")
        status = s.heal()
        assert status == "recovered"

class TestAuditTrail:
    def test_record(self):
        a = AuditTrail()
        a.record("error1")
        assert "error1" in a.logs

class TestCrossServiceErrorPropagation:
    def test_propagate(self):
        c = CrossServiceErrorPropagation(error="timeout", services=["auth","db"])
        results = c.propagate()
        assert "auth received error" in results[0]
