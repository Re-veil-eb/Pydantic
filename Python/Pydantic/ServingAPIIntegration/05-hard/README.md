# Hard Challenges: Transactional APIs

## Scenarios
1. **Transaction** → `/transaction` rolls back on failure.
2. **Batch Processing** → `/batch` allows partial success with error reporting.
3. **Dead Letter Queue** → `/dlq` stores failed requests.
4. **Graceful Shutdown** → Closes DB connections on shutdown.

## Why It Matters
These endpoints simulate enterprise-grade APIs:
- Ensures transactional integrity.
- Allows partial success in batch jobs.
- Provides DLQ for failed requests.
- Ensures clean shutdown of resources.

## Tests
Run `pytest test_main.py` to validate:
- Failed transactions rollback.
- Batch processing returns processed and failed items.
- DLQ stores failed requests.
