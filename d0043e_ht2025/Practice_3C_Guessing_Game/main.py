import random

secret_number = random.randint(1, 20)
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    guess_input_str = input("Guess a number between 1 and 20: ")

    # Validate if it is a digit
    if not guess_input_str.isdigit():
        print("Out of range! Guess again.")
        continue

    # Validate if the number is in range
    guess_input = int(guess_input_str)
    if guess_input < 1 or guess_input > 20:
        print("Out of range! Guess again.")
        continue

    attempts = attempts + 1

    if guess_input > secret_number:
        print("Too High!")
    elif guess_input < secret_number:
        print("Too low!")
    else:
        break

if guess_input == secret_number:
    print(f"Correct! You guessed it in {attempts} attempts.")
else:
    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")