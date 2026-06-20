# Easy Challenges: Date & Time Rules

## Scenarios
1. **Booking** → End date must be after start date.
2. **Event** → End time must be after start time.
3. **Subscription** → Trial period cannot exceed 30 days.
4. **Delivery** → Delivery date must be on or after order date.

## Why It Matters
These rules simulate scheduling and subscription systems:
- Prevents invalid bookings.
- Enforces logical event times.
- Controls trial periods.
- Ensures delivery happens after ordering.

## Tests
Run `pytest test_models.py` to validate:
- Invalid bookings fail.
- Events with reversed times fail.
- Trials longer than 30 days fail.
- Delivery before order date fails.
