# Hard Challenges: Integrity & Capacity Rules

## Scenarios
1. **Flight** → Departure and arrival airports cannot be the same; route code must match.
2. **ConferenceRoomBooking** → Attendees must not exceed room capacity.
3. **InsurancePolicy** → Health coverage requires medical history.
4. **Shipment** → Weight must not exceed max allowed.

## Why It Matters
These rules simulate transport, insurance, and logistics systems:
- Validates flight routes.
- Prevents overbooking rooms.
- Enforces insurance requirements.
- Ensures shipments respect weight limits.

## Tests
Run `pytest test_models.py` to validate:
- Same airport flights fail.
- Over-capacity bookings fail.
- Missing medical history fails.
- Overweight shipments fail.
