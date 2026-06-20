# Very Easy Challenges: Field Metadata & Strict Mode

## Scenarios
1. **Field Metadata** → Use `Field(title, description, example)` for schema docs.
2. **Strict Mode** → Enforce strict types with `ConfigDict(strict=True)`.
3. **Extra Fields** → Forbid unknown fields with `extra="forbid"`.

## Why It Matters
These features improve schema clarity and enforce strict validation:
- Provides rich OpenAPI documentation.
- Prevents type coercion errors.
- Blocks unexpected fields for safety.

## Tests
Run `pytest test_models.py` to validate:
- Valid user passes.
- Negative age fails.
- Extra fields are forbidden.
