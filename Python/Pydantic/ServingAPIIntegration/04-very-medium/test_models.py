import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_loan_valid():
    response = client.post("/loan", json={"income":1000,"loan_amount":4000,"collateral":False})
    assert response.status_code == 200

def test_loan_invalid():
    response = client.post("/loan", json={"income":1000,"loan_amount":6000,"collateral":False})
    assert response.status_code == 422

def test_db_conn():
    response = client.get("/db")
    assert "connection" in response.json()
