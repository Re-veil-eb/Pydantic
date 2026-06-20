import pytest
from models import Student, Classroom, School

class TestClassroomStudents:
    def test_valid_classroom(self):
        students = [Student(roll_number=i, name=f"Student{i}") for i in range(1, 5)]
        classroom = Classroom(students=students)
        assert len(classroom.students) == 4

    def test_classroom_over_capacity(self):
        students = [Student(roll_number=i, name=f"Student{i}") for i in range(1, 35)]
        with pytest.raises(ValueError):
            Classroom(students=students)

    def test_duplicate_roll_numbers(self):
        students = [Student(roll_number=1, name="A"), Student(roll_number=1, name="B")]
        with pytest.raises(ValueError):
            Classroom(students=students)
