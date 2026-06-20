import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_chaos_endpoint():
    response = client.get("/chaos")
    assert response.status_code in [200,500]

def test_propagate():
    response = client.get("/propagate?error=timeout&services=auth&services=db")
    data = response.json()
    assert "auth" in data

def test_compliance():
    response = client.get("/compliance")
    assert (data := response.json())
    assert data["immutable"] is True

def test_observability():
    response = client.get("/observability")
    data = response.json()
    assert "metrics" in data and "logs" in data
