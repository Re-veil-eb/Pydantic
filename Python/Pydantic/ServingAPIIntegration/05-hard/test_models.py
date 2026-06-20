import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_transaction_success():
    response = client.post("/transaction", json={"steps":["a","b"],"fail":False})
    assert response.json()["status"] == "success"

def test_transaction_fail():
    response = client.post("/transaction", json={"steps":["a","b"],"fail":True})
    assert response.status_code == 400

def test_batch_processing():
    response = client.post("/batch", json={"items":["ok1","fail2","ok2"]})
    data = response.json()
    assert "fail2" in data["failed"]

def test_dlq():
    response = client.post("/dlq", json={"failed":["msg1","msg2"]})
    assert "msg1" in response.json()["dlq"]
