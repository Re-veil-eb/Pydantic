import pytest
from models import DistributedRetry, PartialSuccess, PaymentError, AuthError, ErrorMetrics

class TestDistributedRetry:
    def test_valid_retry(self):
        d = DistributedRetry(job_id="job1")
        d.retry()
        assert d.attempts == 1

    def test_exceed_retry(self):
        d = DistributedRetry(job_id="job1", attempts=5)
        with pytest.raises(ValueError):
            d.retry()

class TestPartialSuccess:
    def test_summary(self):
        p = PartialSuccess(processed=["a"], failed=["b"])
        summary = p.summary()
        assert "processed" in summary and "failed" in summary

class TestErrorMetrics:
    def test_record_error(self):
        e = ErrorMetrics()
        e.record("PaymentError")
        assert e.error_counts["PaymentError"] == 1
