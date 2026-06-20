# Very Easy Challenges

## Scenario
Basic Pydantic models with simple field constraints:
- User model with username length, email validation, and age range.
- Product model with non-negative price and auto-generated timestamp.

## Why It Matters
These challenges demonstrate foundational Pydantic usage:
- Type enforcement.
- Field constraints.
- Default values with factories.

## Tests
Run `pytest` to validate:
- Username length enforcement.
- Age range validation.
- Price must be >= 0.
