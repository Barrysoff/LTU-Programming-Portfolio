"""
Write a Python program that determines whether a given number is even or odd,
and prints an appropriate message to the user.
"""

def main():
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("That wasn't an integer!")
    else:
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")


if __name__ == "__main__":
    main()