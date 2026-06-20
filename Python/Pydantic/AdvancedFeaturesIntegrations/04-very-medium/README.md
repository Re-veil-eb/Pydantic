# Very Medium Challenges: ORM Mode & Aliasing

## Scenarios
1. **ORM Mode** → Validate SQLAlchemy objects with `from_attributes=True`.
2. **Aliasing** → Use `Field(alias="externalName")`.
3. **Computed Fields** → Add derived fields with `@computed_field`.
4. **Custom Validators** → Reusable validators with `field_validator`.

## Why It Matters
These features integrate Pydantic with real systems:
- ORM mode bridges SQLAlchemy and Pydantic.
- Aliasing supports external naming conventions.
- Computed fields add derived values.
- Validators enforce custom rules.

## Tests
Run `pytest test_models.py` to validate:
- ORM user works.
- Aliased field maps correctly.
- Computed full name is correct.
- Password validation enforces strength.
