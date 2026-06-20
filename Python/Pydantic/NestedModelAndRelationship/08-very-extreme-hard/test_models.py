import pytest
from models import Factory, Warehouse, RetailStore, SupplyChain

class TestSupplyChain:
    def test_valid_supply_chain(self):
        factories = [Factory(name="F1", stock=100)]
        warehouses = [Warehouse(name="W1", stock=100)]
        stores = [RetailStore(name="S1", stock=100)]
        chain = SupplyChain(factories=factories, warehouses=warehouses, stores=stores)
        assert chain.warehouses[0].stock == 100

    def test_negative_stock(self):
        warehouses = [Warehouse(name="W1", stock=-10)]
        with pytest.raises(ValueError):
            SupplyChain(factories=[], warehouses=warehouses, stores=[])

    def test_unbalanced_stock(self):
        factories = [Factory(name="F1", stock=100)]
        warehouses = [Warehouse(name="W1", stock=100)]
        stores = [RetailStore(name="S1", stock=90)]
        with pytest.raises(ValueError):
            SupplyChain(factories=factories, warehouses=warehouses, stores=stores)
