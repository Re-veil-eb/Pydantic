# Very Hard Challenges: Library Integrations

## Scenarios
1. **SQLAlchemy Integration** → Map ORM models to Pydantic schemas.
2. **Celery Payloads** → Validate task payloads.
3. **Kafka Messages** → Validate message structure.
4. **Airflow Configs** → Validate DAG configs.

## Why It Matters
These features integrate Pydantic with enterprise systems:
- ORM integration bridges DB and API.
- Celery payload validation ensures task safety.
- Kafka message validation ensures event integrity.
- Airflow config validation ensures DAG correctness.

## Tests
Run `pytest test_models.py` to validate:
- ORM schema works.
- Celery payload validates.
- Kafka message validates.
- Airflow config validates.
