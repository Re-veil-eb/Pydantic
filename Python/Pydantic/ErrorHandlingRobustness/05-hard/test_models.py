import pytest
from models import TransactionRollback, MultiErrorAggregation, DeadLetterQueue, GracefulShutdown

class TestTransactionRollback:
    def test_failed_transaction(self):
        t = TransactionRollback(steps=["a","b"], failed_step="b")
        with pytest.raises(ValueError):
            t.execute()

class TestMultiErrorAggregation:
    def test_multiple_errors(self):
        m = MultiErrorAggregation(errors=["e1","e2"])
        with pytest.raises(ValueError):
            m.aggregate()

class TestDeadLetterQueue:
    def test_add_message(self):
        d = DeadLetterQueue()
        d.add("failed message")
        assert "failed message" in d.failed_messages

class TestGracefulShutdown:
    def test_shutdown(self):
        g = GracefulShutdown(resources=["db","cache"])
        assert "db" in g.shutdown()
