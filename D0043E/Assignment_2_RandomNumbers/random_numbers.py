"""
Random Numbers
Mandatory Assignment 2, D0043E
Author: Mattias Westermark
"""

import random

# --- Constants ---
MIN_RANDOM = 0
MAX_RANDOM = 999
INVALID_INPUT_MESSAGE = "Invalid Input"


def how_many_numbers():
    """
    How many numbers asks the user for how many random numbers we want to generate.
    """
    while True:
        how_many_numbers_str = input(f"How many random numbers in the range {MIN_RANDOM} - {MAX_RANDOM} are desired? ")
        try:
            how_many_numbers_int = int(how_many_numbers_str)
            if how_many_numbers_int >= 1:
                return how_many_numbers_int
            else:
                print(f"{INVALID_INPUT_MESSAGE}")
        except ValueError:
            print(f"{INVALID_INPUT_MESSAGE}")
            continue


def generate_numbers(total_numbers):
    """
    Generate the required number of random numbers in the defined range, MIN_RANDOM to MAX_RANDOM
    """
    random_numbers = []

    for _ in range(total_numbers):
        random_numbers.append(random.randint(MIN_RANDOM, MAX_RANDOM))
    return random_numbers


def split_list(random_list):
    """
    Split the list of generated numbers into two lists, one with even and one with odd numbers
    """
    even_numbers = []
    odd_numbers = []

    for num in (random_list):
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers


def bubble_sort(numbers):
    """
    Classic bubble sort from lowest to highest number
    """
    result = numbers[:]
    n = len(result)

    # Outer loop
    for i in range(0, n):
        # Inner loop
        for j in range(0, n - i - 1):
            # Compare ajacent elements
            if result[j] > result[j + 1]:
                # Traditional swap
                temp = result[j]
                result[j] = result[j + 1]
                result[j + 1] = temp

    return result


def bubble_sort_decr(numbers):
    """
    A reverse bubble sort, from highest to lowest number
    """
    result = numbers[:]
    n = len(result)

    # Outer loop
    for i in range(0, n):
        # Inner loop
        for j in range(0, n - i - 1):
            # Compare ajacent elements
            if result[j] < result[j + 1]:
                # Traditional swap
                temp = result[j]
                result[j] = result[j + 1]
                result[j + 1] = temp

    return result


def main():
    """
    1. Call how_many_numbers() to get the amount of random numbers to be generated.
    2. Generate a list of random numbers.
    3. Split the list of random numbers, one with odd and one with even numbers.
    4. Sort the lists in ascending and descending order.
    5. Present the results.
    """
    total_numbers = how_many_numbers()
    try:
        random_list = generate_numbers(total_numbers)
        print("\nHere are the random numbers:")
        n = len(random_list)
        for i in range(n):
            if i == n - 1:
                print(random_list[i])
            else:
                print(random_list[i], end=" ")
        even_numbers, odd_numbers = split_list(random_list)
        sorted_even_numbers = bubble_sort(even_numbers)
        sorted_odd_numbers = bubble_sort_decr(odd_numbers)

        print("\nHere are the random numbers arranged:")
        if len(sorted_even_numbers) == 0:
            print("No Even Numbers", end=" ")
        else:
            n = len(sorted_even_numbers)
            for i in range(n):
                print(sorted_even_numbers[i], end=" ")

        print("-", end=" ")

        if len(sorted_odd_numbers) == 0:
            print("No Odd Numbers")
        else:
            n = len(sorted_odd_numbers)
            for i in range(n):
                if i == n - 1:
                    print(sorted_odd_numbers[i])
                else:
                    print(sorted_odd_numbers[i], end=" ")

        print(f"\nOf the above {total_numbers} numbers, {len(sorted_even_numbers)} were even and {len(sorted_odd_numbers)} odd")

    except MemoryError:
        print("Impossible to handle the requested amount of numbers on this system.")


# Run the program
if __name__ == "__main__":
    main()
