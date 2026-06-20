# Hard Challenges: Advanced Serialization & Immutability

## Scenarios
1. **Nested Generics** → `Response[List[T]]`.
2. **Custom Error Messages** → Override default errors.
3. **Advanced Serialization** → Custom encoders for Decimal, datetime.
4. **Immutable Models** → `ConfigDict(frozen=True)`.

## Why It Matters
These features enforce enterprise-grade rules:
- Nested generics support complex responses.
- Custom errors improve clarity.
- Serialization handles advanced types.
- Immutable models prevent accidental changes.

## Tests
Run `pytest test_models.py` to validate:
- Nested generics work.
- Custom error messages trigger.
- Decimal serialization works.
- Immutable models cannot be modified.
