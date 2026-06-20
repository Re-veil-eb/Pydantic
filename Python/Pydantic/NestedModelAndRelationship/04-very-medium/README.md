# Very Medium Challenge: School and Classrooms

## Scenario
- A `School` contains multiple `Classroom`s.
- Each `Classroom` contains `Student`s.
- Classrooms cannot exceed 30 students.
- Roll numbers must be unique within a classroom.

## Why It Matters
Simulates education systems:
- Enforces capacity limits.
- Prevents duplicate student records.

## Tests
Run `pytest test_models.py` to validate:
- Over-capacity classrooms fail.
- Duplicate roll numbers fail.
