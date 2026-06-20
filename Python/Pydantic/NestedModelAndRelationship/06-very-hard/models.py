from pydantic import BaseModel, field_validator
from typing import List

class Task(BaseModel):
    task_id: str
    depends_on: List[str] = []

class Project(BaseModel):
    tasks: List[Task]

    @field_validator("tasks")
    @classmethod
    def validate_dependencies(cls, tasks):
        task_ids = {t.task_id for t in tasks}
        for task in tasks:
            for dep in task.depends_on:
                if dep not in task_ids:
                    raise ValueError(f"Dependency {dep} not found")
        # Detect circular dependencies (simplified)
        visited = set()
        def dfs(task_id, stack):
            if task_id in stack:
                raise ValueError("Circular dependency detected")
            stack.add(task_id)
            for dep in next(t for t in tasks if t.task_id == task_id).depends_on:
                dfs(dep, stack)
            stack.remove(task_id)
        for t in tasks:
            dfs(t.task_id, set())
        return tasks
