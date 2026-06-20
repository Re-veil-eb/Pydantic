import pytest
from models import Service, MicroserviceConfig

class TestMicroserviceConfig:
    def test_valid_config(self):
        services = [
            Service(name="gateway", entrypoint=True),
            Service(name="auth", dependencies=["gateway"]),
        ]
        config = MicroserviceConfig(services=services)
        assert any(s.entrypoint for s in config.services)

    def test_missing_dependency(self):
        services = [Service(name="auth", dependencies=["gateway"])]
        with pytest.raises(ValueError):
            MicroserviceConfig(services=services)

    def test_cyclic_dependency(self):
        services = [
            Service(name="A", dependencies=["B"]),
            Service(name="B", dependencies=["A"]),
        ]
        with pytest.raises(ValueError):
            MicroserviceConfig(services=services)

    def test_no_entrypoint(self):
        services = [Service(name="auth")]
        with pytest.raises(ValueError):
            MicroserviceConfig(services=services)
