def get_grades():
    print("Write the grades separated by space:")
    grades_input = input().split()
    return convert_grades_to_normal_form(grades_input)


def convert_grades_to_normal_form(grades):
    verify_grades = []
    for grade in grades:
        verify_grade_by_type(grade)
        verify_grade_by_value(grade)
        verify_grades.append(int(grade) if grade.isdigit() else float(grade))
    return verify_grades


def verify_grade_by_value(grade):
    grade = float(grade)
    if grade < 2 or grade > 5:
        raise ValueError("Grade must be between 2 and 5")


def verify_grade_by_type(grade):
    if not isinstance(grade, str) and (grade.isdigit() or grade.replace('.', '').isdigit()):
        raise ValueError("Grades must have type int or float")


def calculate_average(marks):
    return sum(marks) / len(marks)


def check_for_grade_2(marks):
    if 2 in marks:
        print("There is a grade of 2.")


def main():
    marks = get_grades()

    average = calculate_average(marks)
    print("Average grade:", average)

    check_for_grade_2(marks)


if __name__ == "__main__":
    main()
