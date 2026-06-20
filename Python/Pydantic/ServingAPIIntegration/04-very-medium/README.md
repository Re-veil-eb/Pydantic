# Very Medium Challenges: Cross-Field Rules & Middleware

## Scenarios
1. **Loan** → `/loan` enforces loan rules (≤5× income unless collateral).
2. **Dependency Injection** → `/db` injects DB connection.
3. **Error Logging Middleware** → Logs all request errors.

## Why It Matters
These endpoints simulate production-grade APIs:
- Enforces financial rules.
- Demonstrates dependency injection.
- Logs errors for debugging and monitoring.

## Tests
Run `pytest test_main.py` to validate:
- Loan exceeding 5× income fails without collateral.
- DB connection is injected.
- Errors are logged by middleware.
