"""
Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
"""

def main():
    num_3 = 0
    try:
        num_1 = int(input("Enter the first, positive, integer: "))
        if num_1 < 0:
            print("That's not a positive number")
            return

        num_2 = int(input("Enter the second, positive, integer: "))
        if num_2 < 0:
            print("That's not a positive number")
            return

    except ValueError:
        print("That's not a valid integer!")
        return

    # Sort the numbers in ascending order

    if num_2 > num_1:
        temp = num_1
        num_1 = num_2
        num_2 = temp

    # Calculate the GCD
    while True:
        if num_2 == 0:
            print(f"GCD = {num_1}.")
            break
        else:
            num_3 = num_1 % num_2
            num_1 = num_2
            num_2 = num_3


if __name__ == "__main__":
    main()
    