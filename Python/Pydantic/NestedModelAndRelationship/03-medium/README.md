# Medium Challenge: Company and Employees

## Scenario
- A `Company` has a list of `Employee`s.
- Employee IDs must be unique.
- At least one employee must have the role "CEO".

## Why It Matters
Models organizational rules:
- Prevents duplicate employee records.
- Ensures leadership is defined.

## Tests
Run `pytest test_models.py` to validate:
- Duplicate employee IDs fail.
- Missing CEO fails.
