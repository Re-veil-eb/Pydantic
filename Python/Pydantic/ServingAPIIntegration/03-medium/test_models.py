import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_order_total():
    response = client.post("/order", json={"products":[{"name":"p1","price":10},{"name":"p2","price":20}]})
    assert response.json()["order_total"] == 30

def test_discount_valid():
    response = client.post("/discount", json={"percentage":10})
    assert response.status_code == 200

def test_discount_invalid():
    response = client.post("/discount", json={"percentage":10,"amount":5})
    assert response.status_code == 422

def test_invoice_valid():
    response = client.post("/invoice", json={"total":30,"items":[10,20]})
    assert response.status_code == 200

def test_invoice_invalid():
    response = client.post("/invoice", json={"total":25,"items":[10,20]})
    assert response.status_code == 422
