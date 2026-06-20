# Very Extreme Hard Challenges: Dynamic Models & Compliance

## Scenarios
1. **Schema Registry** → Generate schemas for Kafka/Avro.
2. **Dynamic Model Creation** → `create_model()` at runtime.
3. **Plugin Architecture** → Extend Pydantic with plugins.
4. **Microservice Integration** → Shared models across services.
5. **Compliance Rules** → GDPR/PCI-DSS validation.

## Why It Matters
These features enable enterprise-grade extensibility:
- Schema registry supports event-driven systems.
- Dynamic models allow runtime flexibility.
- Plugins extend validation logic.
- Shared models unify microservices.
- Compliance rules enforce security standards.

## Tests
Run `pytest test_models.py` to validate:
- Schema registry works.
- Dynamic model validates.
- Plugin model validates.
- Microservice model validates.
- Compliance rules enforce PCI-DSS.
