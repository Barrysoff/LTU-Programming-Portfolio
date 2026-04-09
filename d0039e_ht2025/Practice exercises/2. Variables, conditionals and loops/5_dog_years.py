"""
Write a Python program to calculate a dog's age in dog years.
(For the first two years, a dog year is equal to 10.5 human years.
After that, each dog year equals 4 human years.)
"""

def main():
    dog_age_str = input("How old is your dog? ")

    try:
        dog_age = float(dog_age_str)
    except ValueError:
        print("That is not a valid age!")
        return

    if dog_age < 0:
        print("Your dog isn't even born yet!")
    elif dog_age <= 2:
        print("Your dog is", dog_age * 10.5, "human years old!")
    else:
        result = 2 * 10.5 + (dog_age - 2) * 4
        print(f"Your dog is {result} years old!")


if __name__ == "__main__":
    main()
