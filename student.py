import sys

# Function to calculate grade
def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg <= 89:
        return "A"
    elif 65 <= avg <= 79:
        return "B"
    elif 50 <= avg <= 64:
        return "C"
    elif 40 <= avg <= 49:
        return "D"
    else:
        return "F"

# Function to display result
def get_student_result(name, dept, semester, m1, m2, m3):
    avg = (m1 + m2 + m3) / 3
    grade = calculate_grade(avg)

    result = (
        f"\n--- Student Result ---\n"
        f"Name: {name}\n"
        f"Department: {dept}\n"
        f"Semester: {semester}\n"
        f"Average Marks: {avg:.2f}\n"
        f"Grade: {grade}"
    )

    return result


# 👉 MAIN PROGRAM
if __name__ == "__main__":

    print("=== Student Result Program ===\n")

    # 1️⃣ PRINT GRADE TABLE FIRST
    print("+-----------+---------+")
    print("| Marks     | Grade   |")
    print("+-----------+---------+")
    print("| 90–100    |   S     |")
    print("| 80–89     |   A     |")
    print("| 65–79     |   B     |")
    print("| 50–64     |   C     |")
    print("| 40–49     |   D     |")
    print("| Below 40  |   F     |")
    print("+-----------+---------+\n")

    try:
        # 2️⃣ TAKE INPUT
        if len(sys.argv) == 7:
            name = sys.argv[1]
            dept = sys.argv[2]
            semester = sys.argv[3]
            m1 = int(sys.argv[4])
            m2 = int(sys.argv[5])
            m3 = int(sys.argv[6])
        else:
            name = input("Enter Student Name: ")
            dept = input("Enter Department: ")
            semester = input("Enter Semester: ")
            m1 = int(input("Enter Subject 1 Marks: "))
            m2 = int(input("Enter Subject 2 Marks: "))
            m3 = int(input("Enter Subject 3 Marks: "))

        # 3️⃣ PRINT RESULT
        print(get_student_result(name, dept, semester, m1, m2, m3))

    except ValueError:
        print("Invalid input! Please enter numeric marks.")
