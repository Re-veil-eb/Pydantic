# Extreme Hard Challenges: Resilience Patterns

## Scenarios
1. **ResilientPipeline** → Continue processing even if one stage fails.
2. **AdaptiveRetry** → Retry with exponential backoff.
3. **FailoverMechanism** → Switch to backup service if primary fails.
4. **ErrorCorrelationID** → Attach correlation IDs to errors.

## Why It Matters
These rules simulate resilience patterns:
- Pipelines continue despite failures.
- Adaptive retry prevents overload.
- Failover ensures service continuity.
- Correlation IDs enable tracing.

## Tests
Run `pytest test_models.py` to validate:
- Pipeline continues despite failures.
- Exceeding retries fails.
- Failover switches to backup.
- Correlation IDs are attached.
