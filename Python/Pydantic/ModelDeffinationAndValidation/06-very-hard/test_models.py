import pytest
from models import BankAccount

class TestBankAccount:
    def test_unique_account_number(self):
        with pytest.raises(ValueError):
            BankAccount(account_number="1234567890", balance=100)

    def test_withdraw_success(self):
        acc = BankAccount(account_number="99999", balance=100)
        acc.withdraw(50)
        assert acc.balance == 50

    def test_withdraw_exceeds_balance(self):
        acc = BankAccount(account_number="88888", balance=100)
        with pytest.raises(ValueError):
            acc.withdraw(200)
