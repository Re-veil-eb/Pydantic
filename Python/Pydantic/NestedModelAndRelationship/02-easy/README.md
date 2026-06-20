# Easy Challenge: Orders and Customers

## Scenario
- An `Order` contains multiple `Product`s.
- A `Customer` has a nested `Address` with a validated zip code.

## Why It Matters
Common in e-commerce systems:
- Orders often contain multiple items.
- Address validation ensures data integrity.

## Tests
Run `pytest test_models.py` to validate:
- Orders with multiple products pass.
- Invalid zip codes fail.
