"""
Python Mini Project: Student Grade Calculator
Module 2 - AI/Python Internship

This program takes marks for five subjects, calculates the total,
percentage, and assigns a grade.
"""

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def main():
    print("===== Student Grade Calculator =====")
    subjects = ["Python", "Mathematics", "English", "Computer Science", "Communication"]
    marks = []

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                print("Please enter marks between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks)
    percentage = total / len(subjects)
    grade = calculate_grade(percentage)

    print("\n===== Result =====")
    print(f"Total Marks: {total:.2f}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

    if grade == "F":
        print("Result: Needs Improvement")
    else:
        print("Result: Pass")


if __name__ == "__main__":
    main()
