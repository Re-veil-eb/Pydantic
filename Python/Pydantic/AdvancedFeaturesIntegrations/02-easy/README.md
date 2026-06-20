# Easy Challenges: Serialization & Schema Generation

## Scenarios
1. **Serialization** → `.model_dump()` and `.model_dump_json()`.
2. **Deserialization** → `.model_validate()` from dict/JSON.
3. **Schema Generation** → `.model_json_schema()` for OpenAPI docs.
4. **Default Factory** → Use `Field(default_factory=...)`.

## Why It Matters
These features enable smooth data exchange:
- Serialize models to dict/JSON.
- Deserialize from external sources.
- Generate schemas for documentation.
- Provide default values dynamically.

## Tests
Run `pytest test_models.py` to validate:
- Serialization outputs JSON.
- Deserialization works from dict.
- Schema contains properties.
- Default factory sets token.
