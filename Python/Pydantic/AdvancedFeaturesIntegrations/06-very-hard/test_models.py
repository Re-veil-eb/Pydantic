import pytest
from models import UserSchema, CeleryPayload, KafkaMessage, AirflowConfig

def test_user_schema():
    u = UserSchema(id=1, username="john", email="john@example.com")
    assert u.username == "john"

def test_celery_payload():
    c = CeleryPayload(task_id="t1", payload={"key":"value"})
    assert c.payload["key"] == "value"

def test_kafka_message():
    k = KafkaMessage(topic="topic1", key="k1", value={"msg":"hello"})
    assert k.topic == "topic1"

def test_airflow_config():
    a = AirflowConfig(dag_id="dag1", schedule="daily")
    assert a.dag_id == "dag1"
