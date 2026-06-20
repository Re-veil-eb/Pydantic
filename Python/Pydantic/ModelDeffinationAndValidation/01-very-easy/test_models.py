import pytest
from models import User, Product

class TestUser:
    def test_valid_user(self):
        user = User(username="john_doe", email="john@example.com", age=30)
        assert user.username == "john_doe"

    def test_invalid_username_length(self):
        with pytest.raises(ValueError):
            User(username="ab", email="john@example.com", age=30)

    def test_invalid_age(self):
        with pytest.raises(ValueError):
            User(username="john_doe", email="john@example.com", age=150)

class TestProduct:
    def test_valid_product(self):
        product = Product(price=10.5)
        assert product.price == 10.5

    def test_negative_price(self):
        with pytest.raises(ValueError):
            Product(price=-5)
