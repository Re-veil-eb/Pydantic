# Medium Challenges: Nested Models & Custom Errors

## Scenarios
1. **Order** → `/order` accepts nested Product models and calculates total.
2. **Discount** → `/discount` enforces mutually exclusive fields.
3. **Custom Error Handling** → Wraps validation errors into JSON.
4. **Invoice** → `/invoice` validates invoice totals.

## Why It Matters
These endpoints simulate real business logic:
- Nested models for orders.
- Mutually exclusive discounts.
- Structured error responses.
- Invoice validation ensures integrity.

## Tests
Run `pytest test_main.py` to validate:
- Order totals are correct.
- Discounts with both fields fail.
- Invoice totals must match items.
