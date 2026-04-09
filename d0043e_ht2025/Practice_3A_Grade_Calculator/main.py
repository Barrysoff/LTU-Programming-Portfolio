def get_score(subject):
    while True:
        str_score = input(f"Enter the score for Subject {subject}: ")
        if str_score.isdigit():
            subject_score = float(str_score)
            break
        else:
            print("Invalid integer, enter a valid integer")

    return subject_score


subject1 = get_score(1)
subject2 = get_score(2)
subject3 = get_score(3)
subject4 = get_score(4)
subject5 = get_score(5)

average = (subject1 + subject2 + subject3 + subject4 + subject5) / 5

grade = ""

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("\nGrade Report")
print("----------------------")

print(f"Subject 1: {subject1}")
print(f"Subject 2: {subject2}")
print(f"Subject 3: {subject3}")
print(f"Subject 4: {subject4}")
print(f"Subject 5: {subject5}")

print(f"\nAverage Score: {average:.2f}")
print(f"Final Grade: {grade}")