# Very Extreme Hard Challenges: Compliance & Integrity Rules

## Scenarios
1. **HealthcareRecord** → Prescriptions must be signed by the doctor, covered by insurance, and age-appropriate.
2. **BankingTransaction** → Debits and credits must balance.
3. **SupplyChainAudit** → Shipments must reconcile with warehouse stock.

## Why It Matters
These challenges simulate enterprise-grade compliance:
- Healthcare systems must enforce medical and insurance rules.
- Banking requires strict double-entry accounting.
- Supply chains must reconcile shipments with inventory.

## Tests
Run `pytest test_models.py` to validate:
- Unsigned prescriptions fail.
- Uncovered drugs fail.
- Age-inappropriate treatments fail.
- Unbalanced transactions fail.
- Shipments not matching warehouse stock fail.
