# Extreme Hard Challenge: Microservice Config

## Scenario
- A `MicroserviceConfig` contains multiple `Service`s.
- Services must declare valid dependencies.
- Cyclic dependencies are forbidden.
- At least one service must be entrypoint=True.

## Why It Matters
Simulates distributed system configs:
- Ensures dependency graphs are valid.
- Guarantees a clear entrypoint for the system.

## Tests
Run `pytest test_models.py` to validate:
- Missing dependencies fail.
- Cyclic dependencies fail.
- No entrypoint fails.
