# Very Medium Challenges: Cross-Field Business Rules

## Scenarios
1. **EmployeeCompensation** → Bonus cannot exceed 20% of salary.
2. **CourseEnrollment** → End date must be within semester.
3. **VehicleRegistration** → Electric vehicles must declare battery capacity.
4. **Membership** → Premium membership requires payment info.

## Why It Matters
These rules simulate HR, education, automotive, and membership systems:
- Enforces compensation policies.
- Validates course timelines.
- Requires electric vehicle details.
- Ensures premium memberships have payment info.

## Tests
Run `pytest test_models.py` to validate:
- Excessive bonus fails.
- Course beyond semester fails.
- Missing battery capacity fails.
- Premium membership without payment fails.
