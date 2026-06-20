# Very Easy Challenges: Basic API Endpoints

## Scenarios
1. **Ping Endpoint** → `/ping` returns "pong".
2. **User Model Serving** → `/user` accepts a User model and returns it back.
3. **Echo Service** → `/echo` returns the same payload sent.

## Why It Matters
These are the simplest API endpoints:
- Validates basic FastAPI setup.
- Demonstrates request/response handling.
- Provides echo service for debugging.

## Tests
Run `pytest test_main.py` to validate:
- `/ping` returns pong.
- `/user` returns submitted user.
- `/echo` returns identical payload.
