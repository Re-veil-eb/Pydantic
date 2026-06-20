# Easy Challenges: Graceful Failures & Fallbacks

## Scenarios
1. **RetryCounter** → Track retries for failed API calls, max 3 allowed.
2. **GracefulTimeout** → Timeout must not exceed 30 seconds.
3. **FallbackValue** → Default currency to USD if missing.
4. **ValidationErrorWrapper** → Wrap validation errors into a custom response.

## Why It Matters
These rules simulate common backend resilience patterns:
- Prevents infinite retries.
- Enforces timeout thresholds.
- Provides default values for missing fields.
- Wraps errors into structured responses.

## Tests
Run `pytest test_models.py` to validate:
- Retry beyond 3 fails.
- Timeout >30 fails.
- Currency defaults to USD.
- Empty values trigger validation errors.
