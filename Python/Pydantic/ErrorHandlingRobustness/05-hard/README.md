# Hard Challenges: Transaction & Aggregation Rules

## Scenarios
1. **TransactionRollback** → Rollback if any step fails.
2. **MultiErrorAggregation** → Collect multiple errors and return together.
3. **DeadLetterQueue** → Failed messages sent to DLQ.
4. **GracefulShutdown** → Close resources cleanly on fatal error.

## Why It Matters
These rules simulate enterprise-grade error handling:
- Ensures transactional integrity.
- Aggregates multiple errors for debugging.
- Provides DLQ for failed messages.
- Ensures clean shutdown of resources.

## Tests
Run `pytest test_models.py` to validate:
- Failed transactions rollback.
- Multiple errors aggregated.
- DLQ stores failed messages.
- Shutdown closes resources.
