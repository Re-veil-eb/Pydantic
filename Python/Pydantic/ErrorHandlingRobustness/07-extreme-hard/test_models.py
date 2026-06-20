import pytest
from models import ResilientPipeline, AdaptiveRetry, FailoverMechanism, ErrorCorrelationID

class TestResilientPipeline:
    def test_run_pipeline(self):
        r = ResilientPipeline(stages=["stage1","stage2"])
        results = r.run()
        assert "Stage stage1 succeeded" in results[0]

class TestAdaptiveRetry:
    def test_exceed_retry(self):
        a = AdaptiveRetry(attempts=5)
        with pytest.raises(ValueError):
            a.retry()

class TestFailoverMechanism:
    def test_primary(self):
        f = FailoverMechanism(primary=True)
        assert "Primary" in f.execute()

    def test_failover(self):
        f = FailoverMechanism(primary=False)
        assert "backup" in f.execute()

class TestErrorCorrelationID:
    def test_trace(self):
        e = ErrorCorrelationID(error_id="123", message="Failure")
        assert "[123]" in e.trace()
