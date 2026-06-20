import pytest
from models import LineItem, Invoice

class TestInvoiceLineItems:
    def test_valid_invoice(self):
        items = [LineItem(description="Item1", total=50), LineItem(description="Item2", total=50)]
        invoice = Invoice(invoice_total=100, line_items=items)
        assert invoice.invoice_total == 100

    def test_mismatched_total(self):
        items = [LineItem(description="Item1", total=50), LineItem(description="Item2", total=40)]
        with pytest.raises(ValueError):
            Invoice(invoice_total=100, line_items=items)
