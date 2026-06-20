# Medium Challenges

## Scenario
Models with union types and custom validators:
- Transaction model where amount can be str or float.
- Discount must not exceed 100.
- Currency must be one of USD, EUR, INR.

## Why It Matters
Demonstrates:
- Union type handling.
- Custom validators for business rules.
- Case normalization and strict value enforcement.

## Tests
Run `pytest` to validate:
- Amount coercion from str to float.
- Discount validation.
- Currency normalization and enforcement.
