import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_retry_success():
    response = client.post("/retry", json={"job_id":"job1","attempts":2})
    assert response.json()["attempts"] == 3

def test_retry_fail():
    response = client.post("/retry", json={"job_id":"job1","attempts":6})
    assert "error" in response.json()

def test_failover_primary():
    response = client.get("/failover?primary=true")
    assert "primary" in response.json()["status"]

def test_failover_backup():
    response = client.get("/failover?primary=false")
    assert "backup" in response.json()["status"]

def test_metrics():
    response = client.get("/metrics")
    assert "errors" in response.json()
