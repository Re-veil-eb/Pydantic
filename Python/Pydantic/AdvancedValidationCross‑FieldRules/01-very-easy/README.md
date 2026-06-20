# Very Easy Challenges: Basic Cross-Field Rules

## Scenarios
1. **RegistrationForm** → Password and confirm_password must match.
2. **AgeCheck** → User must be at least 18 years old.
3. **EmailSignup** → Email must contain @ and domain.

## Why It Matters
These are common validation rules in signup flows and user onboarding:
- Prevents mismatched passwords.
- Enforces age restrictions.
- Ensures valid email formats.

## Tests
Run `pytest test_models.py` to validate:
- Password mismatch fails.
- Underage users fail.
- Invalid email format fails.
