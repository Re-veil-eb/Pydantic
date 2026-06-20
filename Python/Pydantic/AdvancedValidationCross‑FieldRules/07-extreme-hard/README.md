# Extreme Hard Challenges: Scheduling & Overlap Rules

## Scenarios
1. **ConferenceSchedule** → Sessions cannot overlap in time.
2. **ProjectTimeline** → Tasks must fit within project start/end dates.
3. **ShiftSchedule** → Doctors cannot be assigned overlapping shifts.

## Why It Matters
These challenges simulate real-world scheduling systems:
- Conferences require non-overlapping sessions.
- Projects must keep tasks within defined timelines.
- Hospitals must prevent overlapping shifts for the same doctor.

## Tests
Run `pytest test_models.py` to validate:
- Valid schedules pass.
- Overlapping sessions fail.
- Tasks outside project timeline fail.
- Overlapping doctor shifts fail.
