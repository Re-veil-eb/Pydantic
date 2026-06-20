# Medium Challenges: Mutually Exclusive & Conditional Rules

## Scenarios
1. **Discount** → Only one of percentage or amount can be set.
2. **Payment** → Card number requires expiry date and CVV.
3. **ProfileUpdate** → Updating email resets verification.
4. **Reservation** → Guest count must not exceed max capacity.

## Why It Matters
These rules simulate business logic in commerce and user systems:
- Prevents conflicting discounts.
- Enforces complete payment info.
- Resets verification when email changes.
- Ensures reservations respect capacity limits.

## Tests
Run `pytest test_models.py` to validate:
- Discounts with both fields fail.
- Missing card info fails.
- Email update resets verification.
- Over-capacity reservations fail.
