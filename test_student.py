import pytest
from student import get_student_result

def test_student_grade_A():
    # Input data
    name = "anannya"
    dept = "bca"
    semester = "3"
    m1 = 80
    m2 = 85
    m3 = 90

    # Expected output (matches exactly what get_student_result() returns)
    expected_output = (
        "\n--- Student Result ---\n"
        "Name: anannya\n"
        "Department: bca\n"
        "Semester: 3\n"
        "Average Marks: 85.00\n"
        "Grade: A"
    )

    # Assertion
    assert get_student_result(name, dept, semester, m1, m2, m3) == expected_output
