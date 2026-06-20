import pytest
from models import Product, Order, Address, Customer

class TestOrder:
    def test_valid_order(self):
        products = [Product(name="Book", price=10), Product(name="Pen", price=2)]
        order = Order(products=products)
        assert len(order.products) == 2

class TestCustomerAddress:
    def test_valid_customer(self):
        addr = Address(street="123 Main St", city="NYC", zip="12345")
        cust = Customer(name="Alice", address=addr)
        assert cust.address.zip == "12345"

    def test_invalid_zip(self):
        with pytest.raises(ValueError):
            Address(street="123 Main St", city="NYC", zip="12AB")
