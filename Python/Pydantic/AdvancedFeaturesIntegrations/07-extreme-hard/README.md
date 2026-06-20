# Extreme Hard Challenges: Root Models & Schema Customization

## Scenarios
1. **Custom Root Types** → Models that wrap lists/dicts.
2. **Advanced Generics** → PositiveIntResponse[T].
3. **Schema Customization** → Add examples, descriptions, deprecations.
4. **Cross-Library Integration** → Pydantic with other libraries.

## Why It Matters
These features extend Pydantic flexibility:
- Root models wrap raw lists/dicts.
- Generics enforce constraints.
- Schema customization improves docs.
- Cross-library integration supports hybrid systems.

## Tests
Run `pytest test_models.py` to validate:
- Root model works.
- PositiveIntResponse enforces >0.
- Schema customization applies.
- Cross-library model validates.
