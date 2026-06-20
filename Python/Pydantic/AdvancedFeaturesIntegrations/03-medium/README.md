# Medium Challenges: Generics & Custom Types

## Scenarios
1. **Generic Models** → `PaginatedResponse[T]` with `TypeVar`.
2. **Constrained Types** → `constr`, `conint`, `conlist`.
3. **Standard Types** → `EmailStr`, `HttpUrl`.
4. **Union Types** → Accept multiple input formats.

## Why It Matters
These features enforce strong typing:
- Generics allow reusable response wrappers.
- Constrained types enforce ranges and lengths.
- Standard types validate emails and URLs.
- Union types support flexible inputs.

## Tests
Run `pytest test_models.py` to validate:
- Paginated response works.
- Custom types enforce rules.
- Invalid age fails.
