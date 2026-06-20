# Very Hard Challenge: BankAccount Model

## Scenario
Bank account validation:
- Account number must be unique.
- Withdrawals must not exceed balance.
- Idempotency enforced for repeated requests.

## Why It Matters
Simulates financial system rules:
- Prevents duplicate accounts.
- Protects against overdrafts.
- Ensures consistent state updates.

## Tests
Run `pytest` to validate:
- Duplicate account numbers fail.
- Withdrawals succeed only if balance is sufficient.
- Invalid withdrawal amounts fail.
