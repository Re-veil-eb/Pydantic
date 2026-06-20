# Very Medium Challenges: Structured Error Handling

## Scenarios
1. **APIResponseValidator** → Response must contain required keys.
2. **CircuitBreaker** → Trigger after 5 consecutive failures.
3. **ErrorLogging** → Log errors to a file.
4. **StructuredError** → Return errors in JSON format.

## Why It Matters
These rules simulate structured error handling:
- Validates API responses.
- Prevents cascading failures with circuit breaker.
- Logs errors for debugging.
- Provides machine-readable error responses.

## Tests
Run `pytest test_models.py` to validate:
- Missing keys fail.
- Circuit breaker triggers after 5 failures.
- Errors are logged to file.
- JSON error format is correct.
