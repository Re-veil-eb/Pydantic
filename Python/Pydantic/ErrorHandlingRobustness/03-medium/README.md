# Medium Challenges: Domain-Specific Errors

## Scenarios
1. **Payment** → Amount must be >0, otherwise raise PaymentError.
2. **WebhookRetry** → Retry webhook validation up to 3 times.
3. **DatabaseConnection** → Connection string must start with db://.
4. **GracefulDegradation** → If service unavailable, continue with limited functionality.

## Why It Matters
These rules simulate production-grade error handling:
- Prevents invalid payments.
- Controls webhook retries.
- Validates database connections.
- Allows degraded service instead of total failure.

## Tests
Run `pytest test_models.py` to validate:
- Invalid payment fails.
- Webhook retries beyond 3 fail.
- Invalid connection strings fail.
- Service degradation returns fallback message.
