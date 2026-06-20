# Very Extreme Hard Challenges: Enterprise-Grade APIs

## Scenarios
1. **Global Error Handler** → Centralized error handling across endpoints.
2. **Chaos Testing** → `/chaos` injects random failures.
3. **Cross-Service Error Propagation** → `/propagate` propagates errors across services.
4. **Compliance Logging** → `/compliance` returns immutable logs.
5. **Enterprise Observability** → `/observability` exposes metrics, logs, and tracing.

## Why It Matters
These endpoints simulate enterprise-grade robustness:
- Provides centralized error handling.
- Tests resilience with chaos engineering.
- Propagates errors across services.
- Maintains compliance with immutable logs.
- Exposes observability data for monitoring.

## Tests
Run `pytest test_main.py` to validate:
- Global handler catches errors.
- Chaos endpoint sometimes fails.
- Errors propagate across services.
- Compliance logs are immutable.
- Observability returns metrics, logs, and tracing.
