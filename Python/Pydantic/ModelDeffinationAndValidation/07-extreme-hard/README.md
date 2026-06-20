# Extreme Hard Challenge: DistributedJob Model

## Scenario
Distributed job orchestration:
- Job ID must be UUID.
- Status transitions must follow finite state machine rules.
- Retry count increments only on failure.
- Metadata validated against dynamic JSON schema.

## Why It Matters
Models real distributed systems:
- Enforces workflow integrity.
- Supports retries and error handling.
- Validates dynamic metadata schemas.

## Tests
Run `pytest` to validate:
- Valid metadata passes.
- Missing required fields fail.
- Invalid state transitions fail.
- Retry count increments correctly.
