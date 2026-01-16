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

        print(f"\nStudent Name : {name}")
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

num_students = int(input("Enter number of students: "))

for _ in range(num_students):
    name = input("\nEnter student name: ")
    num_subjects = int(input("Enter number of subjects: "))

    subjects = {}
    for _ in range(num_subjects):
        subject = input("Subject name: ")
        mark = int(input("Marks (0-100): "))
        subjects[subject] = mark

    students[name] = subjects

analyze_students(students)
