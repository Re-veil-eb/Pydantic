import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_success():
    response = client.post("/register", json={"username":"john","password":"123","confirm_password":"123"})
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_register_fail():
    response = client.post("/register", json={"username":"john","password":"123","confirm_password":"456"})
    assert response.status_code == 422  # validation error

def test_profile_default_nickname():
    response = client.post("/profile", json={"username":"john"})
    assert response.json()["profile"]["nickname"] == "john"

def test_search_query():
    response = client.get("/search?query=abc")
    assert response.json()["query"] == "abc"

def test_get_item():
    response = client.get("/items/5")
    assert response.json()["item_id"] == 5
