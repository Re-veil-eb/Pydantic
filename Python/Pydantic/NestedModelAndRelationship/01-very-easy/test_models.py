import pytest
from models import User, Profile, Product, Category

class TestUserProfile:
    def test_valid_user_profile(self):
        profile = Profile(bio="Developer", website="https://example.com")
        user = User(username="john_doe", profile=profile)
        assert user.profile.website == "https://example.com"

class TestProductCategory:
    def test_valid_product_category(self):
        category = Category(name="Electronics")
        product = Product(name="Laptop", category=category)
        assert product.category.name == "Electronics"
