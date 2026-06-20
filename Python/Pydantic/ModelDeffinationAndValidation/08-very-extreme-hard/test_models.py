import pytest
from models import MultiTenantUser, LedgerEntry

class TestMultiTenantUser:
    def test_valid_admin(self):
        user = MultiTenantUser(tenant_id="tenant-abc", role="admin")
        assert user.mfa_enabled is True

    def test_invalid_tenant(self):
        with pytest.raises(ValueError):
            MultiTenantUser(tenant_id="tenant-123", role="admin")

    def test_invalid_role(self):
        with pytest.raises(ValueError):
            MultiTenantUser(tenant_id="tenant-abc", role="manager")

class TestLedgerEntry:
    def test_balanced_entry(self):
        entry = LedgerEntry(debits=100, credits=100)
        assert entry.debits == entry.credits

    def test_unbalanced_entry(self):
        with pytest.raises(ValueError):
            LedgerEntry(debits=100, credits=90)
