"""
Practice assignment 4B, Student Grade Management System
Author: Mattias Westermark
"""


students = {}


def add_student():
    # Check if a student already exists, otherwise add student and grade.
    while True:
        student_name = input("Enter the student's name: ")
        if student_name == "":
            print("Enter a real name!")
            continue

        if student_name in students:
            print("Error: Student already exists.")
            break

        try:
            student_grade = int(input(f"Enter {student_name}'s grade: "))
        except ValueError:
            print("Invalid grade! Enter a valid grade (1-100).")
            continue

        students[student_name] = [student_grade]
        print(f"{student_name} added successfully!\n")
        break


def update_grade():
    # Check if student is listed and updated selected grade if available.
    while True:
        if students == {}:
            print("No students in the system.\n")
            break

        student_name = input("Enter the student's name: ")
        if student_name not in students:
            print("Error: Student not found.")
            break

        student_grades = students[student_name]
        print(f"Current grades for {student_name}: {student_grades}")

        grade_to_update_str = input("Enter the index of the grade to update (starting from 0): ")
        try:
            grade_to_update = int(grade_to_update_str)
        except ValueError:
            print("Invalid choice!\n")
            break

        if grade_to_update < 0 or grade_to_update >= len(student_grades):
            print("Invalid index! Please try again.\n")
            break

        new_grade_str = input("Enter the new grade: ")
        try:
            new_grade = int(new_grade_str)
            students[student_name][grade_to_update] = new_grade
            print(f"{student_name}'s grade updated successfully!\n")
        except ValueError:
            print("Invalid choice!\n")
        break


def remove_student():
    # Check if the student exists, and remove from dictonary if so.
    while True:
        if students == {}:
            print("No students in the system.\n")
            break

        student_name = input("Enter the student's name to remove: ")

        if student_name not in students:
            print("Error: Student not found.")
            break

        del students[student_name]
        print(f"{student_name} removed successfully!\n")

        break


def display_students():
    # Print all listed students.
    if students == {}:
        print("No students in the system.\n")
    else:
        print("Student Grades:")
        for student, grade in students.items():
            grades = str(grade)[1:-1]
            print(f"{student}: {grades}")
        print("")


def main():
    # Show menu and wait for user interaction.
    while True:
        print("1. Add a new student")
        print("2. Update a grade")
        print("3. Remove a student")
        print("4. Display all students")
        print("5. Quit")

        choice_str = input("Choose an option: ")

        if choice_str == "5":
            print("Goodbye!")
            break
        elif choice_str == "1":
            add_student()
        elif choice_str == "2":
            update_grade()
        elif choice_str == "3":
            remove_student()
        elif choice_str == "4":
            display_students()
        else:
            print("\nInvalid input! Please enter a valid number.\n")
            continue


"""Guard function"""
if __name__ == "__main__":
    main()