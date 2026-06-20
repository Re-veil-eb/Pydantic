# Very Easy Challenges: Basic Error Handling

## Scenarios
1. **SimpleValidationError** → Catch invalid email format and raise a clear error.
2. **RequiredFieldCheck** → Ensure required fields (username, password) are present.
3. **DefaultFallback** → If nickname is missing, default to username.

## Why It Matters
These are the most basic error handling rules:
- Prevents invalid user input.
- Ensures required fields are always provided.
- Provides sensible defaults when optional data is missing.

## Tests
Run `pytest test_models.py` to validate:
- Invalid email format fails.
- Required fields must be present.
- Nickname defaults to username if missing.
