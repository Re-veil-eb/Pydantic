from pydantic import BaseModel, field_validator
from typing import List

class Service(BaseModel):
    name: str
    dependencies: List[str] = []
    entrypoint: bool = False

class MicroserviceConfig(BaseModel):
    services: List[Service]

    @field_validator("services")
    @classmethod
    def validate_services(cls, services):
        names = {s.name for s in services}
        for s in services:
            for dep in s.dependencies:
                if dep not in names:
                    raise ValueError(f"Dependency {dep} not found")
        if not any(s.entrypoint for s in services):
            raise ValueError("At least one service must be entrypoint=True")
        # Detect cycles (simplified)
        visited = set()
        def dfs(service, stack):
            if service.name in stack:
                raise ValueError("Cyclic dependency detected")
            stack.add(service.name)
            for dep in service.dependencies:
                dfs(next(s for s in services if s.name == dep), stack)
            stack.remove(service.name)
        for s in services:
            dfs(s, set())
        return services
