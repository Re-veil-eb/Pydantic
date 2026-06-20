import pytest
from models import Task, Project

class TestProjectTasks:
    def test_valid_project(self):
        tasks = [Task(task_id="A"), Task(task_id="B", depends_on=["A"])]
        project = Project(tasks=tasks)
        assert project.tasks[1].depends_on == ["A"]

    def test_missing_dependency(self):
        tasks = [Task(task_id="A"), Task(task_id="B", depends_on=["C"])]
        with pytest.raises(ValueError):
            Project(tasks=tasks)

    def test_circular_dependency(self):
        tasks = [Task(task_id="A", depends_on=["B"]), Task(task_id="B", depends_on=["A"])]
        with pytest.raises(ValueError):
            Project(tasks=tasks)
