# Very Hard Challenge: Project and Tasks

## Scenario
- A `Project` contains multiple `Task`s.
- Tasks must respect dependencies.
- No circular dependencies allowed.

## Why It Matters
Models workflow integrity:
- Prevents invalid task scheduling.
- Detects circular references in project management.

## Tests
Run `pytest test_models.py` to validate:
- Missing dependencies fail.
- Circular dependencies fail.
