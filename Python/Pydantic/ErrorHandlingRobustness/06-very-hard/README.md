# Very Hard Challenges: Distributed Error Handling

## Scenarios
1. **DistributedRetry** → Retry failed jobs across workers, max 5 attempts.
2. **PartialSuccess** → Allow partial batch processing with error reporting.
3. **CustomExceptionHierarchy** → Define domain-specific exceptions.
4. **ErrorMetrics** → Track error counts for monitoring.

## Why It Matters
These rules simulate distributed systems:
- Prevents infinite retries across workers.
- Allows partial success in batch jobs.
- Provides custom exception hierarchy.
- Tracks error metrics for observability.

## Tests
Run `pytest test_models.py` to validate:
- Exceeding retries fails.
- Partial success returns summary.
- Error metrics increment correctly.
