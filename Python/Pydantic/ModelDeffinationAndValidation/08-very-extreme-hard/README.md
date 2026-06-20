# Very Extreme Hard Challenge: MultiTenantUser & LedgerEntry Models

## Scenario
Multi-tenant SaaS and accounting validation:
- Tenant ID must exist in external system.
- Role must be valid for tenant.
- Admin role requires MFA enabled.
- Ledger entries must balance (debits = credits).

## Why It Matters
Simulates enterprise-grade constraints:
- Multi-tenant role enforcement.
- Security policies for admin users.
- Financial integrity with double-entry accounting.

## Tests
Run `pytest` to validate:
- Invalid tenant IDs fail.
- Invalid roles fail.
- Admin role auto-enforces MFA.
- Ledger entries must balance.
