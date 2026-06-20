import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}

def test_create_user():
    response = client.post("/user", json={"username":"john","email":"john@example.com"})
    assert response.status_code == 200
    assert response.json()["user"]["username"] == "john"

def test_echo():
    payload = {"msg":"hello"}
    response = client.post("/echo", json=payload)
    assert response.json()["echo"] == payload
