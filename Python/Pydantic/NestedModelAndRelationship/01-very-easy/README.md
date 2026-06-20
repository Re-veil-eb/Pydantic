# Very Easy Challenge: Basic Nested Models

## Scenario
- A `User` has a nested `Profile` with bio and website.
- A `Product` belongs to a nested `Category`.

## Why It Matters
This demonstrates the foundation of relational data modeling:
- Nested models validate automatically.
- Useful for representing simple one-to-one relationships.

## Tests
Run `pytest test_models.py` to validate:
- User profile creation works.
- Product category nesting works.
