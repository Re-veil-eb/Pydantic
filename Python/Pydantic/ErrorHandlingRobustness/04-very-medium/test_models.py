import pytest
from models import APIResponseValidator, CircuitBreaker, ErrorLogging, StructuredError

class TestAPIResponseValidator:
    def test_valid_response(self):
        a = APIResponseValidator(response={"status":"ok","data":{}})
        assert "status" in a.response

    def test_missing_key(self):
        with pytest.raises(ValueError):
            APIResponseValidator(response={"status":"ok"})

class TestCircuitBreaker:
    def test_record_failure(self):
        c = CircuitBreaker()
        for _ in range(4):
            c.record_failure()
        assert c.failures == 4

    def test_trigger_breaker(self):
        c = CircuitBreaker(failures=4)
        with pytest.raises(ValueError):
            c.record_failure()

class TestErrorLogging:
    def test_log_error(self, tmp_path):
        file = tmp_path / "errors.log"
        e = ErrorLogging(error_message="Something went wrong")
        e.log_error(file=str(file))
        assert "Something went wrong" in file.read_text()

class TestStructuredError:
    def test_to_json(self):
        s = StructuredError(code=400, message="Bad Request")
        assert '"code": 400' in s.to_json()
