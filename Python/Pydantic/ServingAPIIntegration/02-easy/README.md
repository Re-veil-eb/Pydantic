# Easy Challenges: Basic Validation in APIs

## Scenarios
1. **RegistrationForm** → `/register` validates password confirmation.
2. **Profile Defaults** → `/profile` sets default nickname if missing.
3. **Query Params** → `/search?query=abc` returns query string.
4. **Path Params** → `/items/{item_id}` returns item details.

## Why It Matters
These endpoints show basic validation and parameter handling:
- Enforces password rules.
- Provides sensible defaults.
- Demonstrates query and path parameter usage.

## Tests
Run `pytest test_main.py` to validate:
- Password mismatch fails.
- Nickname defaults to username.
- Query and path params return correct values.
