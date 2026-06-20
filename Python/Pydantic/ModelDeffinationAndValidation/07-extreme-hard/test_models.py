import pytest, uuid
from models import DistributedJob

class TestDistributedJob:
    def test_valid_metadata(self):
        job = DistributedJob(job_id=uuid.uuid4(), metadata={"worker_id": "w1", "region": "us-east"})
        assert job.metadata["worker_id"] == "w1"

    def test_missing_metadata(self):
        with pytest.raises(ValueError):
            DistributedJob(job_id=uuid.uuid4(), metadata={"worker_id": "w1"})

    def test_state_transitions(self):
        job = DistributedJob(job_id=uuid.uuid4(), metadata={"worker_id": "w1", "region": "us-east"})
        job.transition_to("RUNNING")
        assert job.status == "RUNNING"
        job.transition_to("FAILED")
        assert job.retry_count == 1
