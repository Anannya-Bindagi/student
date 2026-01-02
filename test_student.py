import pytest
from student import get_student_result

def test_student_grade_A():
    name = "anannya"
    dept = "bca"
    semester = "3"
    m1 = 80
    m2 = 85
    m3 = 90

    expected_output = (
        "Name: anannya, Department: bca, Semester: 3, "
        "Average: 85.00, Grade: A"
    )

    assert get_student_result(name, dept, semester, m1, m2, m3) == expected_output