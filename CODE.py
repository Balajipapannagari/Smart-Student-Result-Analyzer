def get_integer_input(message, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(message))
            if min_val is not None and value < min_val:
                print(f" Invalid input! Value must be ≥ {min_val}")
            elif max_val is not None and value > max_val:
                print(f" Invalid input! Value must be ≤ {max_val}")
            else:
                return value
        except ValueError:
            print(" Invalid data error! Please enter a numeric value.")


def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def analyze_students(students):
    topper = None
    highest_avg = 0

    for name, subjects in students.items():
        total = sum(subjects.values())
        avg = total / len(subjects)
        grade = calculate_grade(avg)
        result = "Pass" if avg >= 40 else "Fail"

        print("\n------------------------------")
        print(f"Student Name : {name}")
        print("Marks        :", subjects)
        print("Total Marks  :", total)
        print("Average      :", round(avg, 2))
        print("Grade        :", grade)
        print("Result       :", result)

        weak_subjects = [sub for sub, mark in subjects.items() if mark < 40]
        if weak_subjects:
            print("Weak Subjects:", ", ".join(weak_subjects))
        else:
            print("Weak Subjects: None")

        if avg > highest_avg:
            highest_avg = avg
            topper = name

    print("\n==============================")
    print("Class Topper:", topper)
    print("Highest Average:", round(highest_avg, 2))


# -------- Main Program --------
students = {}

num_students = get_integer_input("Enter number of students: ", min_val=1)

for _ in range(num_students):
    name = input("\nEnter student name: ")

    num_subjects = get_integer_input(
        "Enter number of subjects: ", min_val=1
    )

    subjects = {}
    for _ in range(num_subjects):
        subject = input("Subject name: ")

        mark = get_integer_input(
            "Marks (0-100): ", min_val=0, max_val=100
        )

        subjects[subject] = mark

    students[name] = subjects

analyze_students(students)
