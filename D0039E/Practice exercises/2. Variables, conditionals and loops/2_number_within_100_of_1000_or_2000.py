"""
Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""


def main():
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("That wasn't an integer!")
    else:
        if 900 <= number <= 1100:
            print(f"{number} is between 900 and 1100.")
        elif 1900 <= number <= 2100:
            print(f"{number} is between 1900 and 2100")
        else:
            print(f"{number} is not in the interval 900 to 1100 or 1900 to 2100.")


if __name__ == "__main__":
    main()
