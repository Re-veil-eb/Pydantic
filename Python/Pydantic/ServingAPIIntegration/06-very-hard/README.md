# Very Hard Challenges: Distributed Resilience

## Scenarios
1. **Distributed Retry** → `/retry` retries failed jobs across workers.
2. **Failover** → `/failover` switches to backup service if primary fails.
3. **Error Metrics** → `/metrics` exposes error counts.

## Why It Matters
These endpoints simulate distributed systems:
- Prevents infinite retries.
- Provides failover for continuity.
- Exposes metrics for monitoring.

## Tests
Run `pytest test_main.py` to validate:
- Retry increments attempts.
- Failover switches to backup.
- Metrics endpoint returns error counts.
