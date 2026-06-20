# Very Medium Challenges

## Scenario
Payment model with advanced validation:
- Card number must pass Luhn algorithm.
- Expiry date must be in the future.
- CVV must be exactly 3 digits.

## Why It Matters
Simulates real-world payment validation:
- Security checks for card numbers.
- Expiry validation prevents invalid cards.
- Regex enforcement for CVV.

## Tests
Run `pytest` to validate:
- Valid card numbers pass.
- Expired cards fail.
- CVV must be exactly 3 digits.
