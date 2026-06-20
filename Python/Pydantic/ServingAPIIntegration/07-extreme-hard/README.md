# Extreme Hard Challenges: Resilient Pipelines & Correlation IDs

## Scenarios
1. **Resilient Pipeline** → `/pipeline` continues processing despite failures.
2. **Correlation ID Middleware** → Attaches correlation IDs to all responses.
3. **Audit Trail** → `/audit` returns immutable error logs.

## Why It Matters
These endpoints simulate resilience patterns:
- Pipelines continue despite failures.
- Correlation IDs enable tracing.
- Audit trail ensures compliance.

## Tests
Run `pytest test_main.py` to validate:
- Pipeline continues despite failures.
- Correlation ID header is present.
- Audit trail returns logs.
