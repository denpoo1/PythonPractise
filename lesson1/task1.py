def generate_tests_student_grades():
    grades = (4, 5, 3, 4, 5, 2, 3, 4, 2, 2, 2, 2)
    return grades


def sum(grades):
    return sum(grades)


def avg(grades):
    return sum(grades) / len(grades)


def median(grades):
    sorted_grades = sorted(grades)
    n = len(sorted_grades)
    if n % 2 == 0:
        return (sorted_grades[n // 2 - 1] + sorted_grades[n // 2]) / 2
    else:
        return sorted_grades[n // 2]


def max(grades):
    return max(grades)


def min(grades):
    return min(grades)


def convert_to_set(grades):
    return set(grades)


def main():
    grades = generate_tests_student_grades()
    print("Sum:", sum(grades))
    print("Lowest:", min(grades))
    print("Average:", avg(grades))
    print("Median:", median(grades))
    print("Set:", convert_to_set(grades))
    print("Highest:", max(grades))


if __name__ == "__main__":
    main()
