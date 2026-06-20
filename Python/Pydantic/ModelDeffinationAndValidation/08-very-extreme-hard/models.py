from typing import Any
from pydantic import BaseModel, Field , model_validator

# Simulated External Database for Validation
MOCK_EXTERNAL_TENANTS = {
    "tenant-abc": ["admin", "editor", "viewer"],
    "tenant-xyz": ["admin", "manager", "staff"],
}

class MultiTenantUser(BaseModel):
    tenant_id: str
    role: str
    mfa_enabled: bool = False

    @model_validator(mode="before")
    @classmethod
    def validate_tenant_and_role_exists(cls, data: Any) -> Any:
        """Runs BEFORE field parsing to check external API data constraints."""
        if not isinstance(data, dict):
            return data
            
        tenant_id = data.get("tenant_id")
        role = data.get("role")

        # 1. Critical check: tenant_id must exist
        if not tenant_id or tenant_id not in MOCK_EXTERNAL_TENANTS:
            raise ValueError(f"Tenant ID '{tenant_id}' does not exist in external system.")

        # 2. Critical check: role must exist within that specific tenant
        allowed_roles = MOCK_EXTERNAL_TENANTS[tenant_id]
        if role not in allowed_roles:
            raise ValueError(f"Role '{role}' is invalid for tenant '{tenant_id}'. Allowed: {allowed_roles}")

        return data

    @model_validator(mode="after")
    def enforce_admin_mfa(self) -> "MultiTenantUser":
        """Runs AFTER field parsing to enforce cross-field business logic."""
        if self.role == "admin" and not self.mfa_enabled:
            # Automatically upgrade to True instead of failing validation
            self.mfa_enabled = True
        return self


class LedgerEntry(BaseModel):
    # Field validation ensures no negative monetary amounts
    debits: float = Field(..., ge=0.0)
    credits: float = Field(..., ge=0.0)

    @model_validator(mode="after")
    def validate_double_entry(self) -> "LedgerEntry":
        """Ensures the accounting system balances perfectly."""
        if self.debits != self.credits:
            raise ValueError(f"Accounting mismatch: Debits ({self.debits}) must equal Credits ({self.credits}).")
        return self
