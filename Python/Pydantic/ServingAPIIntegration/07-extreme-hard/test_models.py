import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_pipeline():
    response = client.post("/pipeline", json={"stages":["s1","s2"]})
    assert "s1 succeeded" in response.json()["results"][0]

def test_correlation_id_header():
    response = client.post("/pipeline", json={"stages":["s1"]})
    assert "X-Correlation-ID" in response.headers

def test_audit():
    response = client.post("/audit", json={"logs":["error1","error2"]})
    assert "error1" in response.json()["audit"]
