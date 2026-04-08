"""
Dice Game 12
Mandatory Assignment 1, D0043E
Author: Mattias Westermark
"""

import random


def print_welcome():
    """Prints a welcome message and explains the rules of Dice Game 12."""
    print("Welcome to dice game 12. You must roll 1-3 dice and try to get the sum of 12 ...\n")


def read_choice(rolled1, rolled2, rolled3):
    """Asks the user to select die to cast or quit."""
    while True:
        """Continue until a valid choice is made. Also check that the dice hasn't been cast already."""
        choice_str = input("Enter which dice you want to roll [1,2,3] (exit with q): ")

        if choice_str.lower() == "q":
            return "q"
        elif not choice_str.isdigit():
            print("Sorry, that is an invalid entry. Try again. Valid entries are 1, 2, 3, and q\n")
            continue

        choice_int = int(choice_str)

        if choice_int not in range(1, 4):
            print("Sorry, that is an invalid entry. Try again. Valid entries are 1, 2, 3, and q\n")
            continue
        if choice_int == 1 and rolled1:
            print("Sorry, you have already rolled that dice. Try again")
            continue
        elif choice_int == 2 and rolled2:
            print("Sorry, you have already rolled that dice. Try again")
            continue
        elif choice_int == 3 and rolled3:
            print("Sorry, you have already rolled that dice. Try again")
            continue
        else:
            return choice_int


def roll_die():
    """Simulate the cast of a die, returning a value from 1 to 6."""
    return random.randint(1, 6)


def show_state(d1, d2, d3, wins, losses):
    """Present the dice values as well as the sum of the three dices. Also present the number of wins and losses."""
    total = d1 + d2 + d3
    print(f"{d1} {d2} {d3} sum: {total} #win: {wins} #loss: {losses}")


def play_round(wins, losses):
    """Set start values for dices, cast dice and number of rolls."""
    d1 = 0
    d2 = 0
    d3 = 0

    rolled1 = False
    rolled2 = False
    rolled3 = False

    rolls_done = 0

    while rolls_done < 3:
        """Plays a single round of Dice Game 12, loop up to three times for number of casts."""
        choice = read_choice(rolled1, rolled2, rolled3)

        if choice == "q":
            print(f"#win: {wins} #loss: {losses}")
            print("Game Over!")
            return "q"
        else:
            """Set selected dice value and mark dice as rolled."""
            die_result = roll_die()
            if choice == 1:
                d1 = die_result
                rolled1 = True
            elif choice == 2:
                d2 = die_result
                rolled2 = True
            else:
                d3 = die_result
                rolled3 = True

        rolls_done = rolls_done + 1

        if rolls_done < 3:
            show_state(d1, d2, d3, wins, losses)
        else:
            total = d1 + d2 + d3
            if total == 12:
                wins = wins + 1
                show_state(d1, d2, d3, wins, losses)
                print("You won!!\n")
                return "win"
            elif total > 12:
                losses = losses + 1
                show_state(d1, d2, d3, wins, losses)
                print("You lost!!\n")
                return "loss"
            else:
                show_state(d1, d2, d3, wins, losses)
                print("You neither won nor lost the game.\n")
                return "none"


def main():
    """Main game loop, loops until user quits."""
    wins = 0
    losses = 0

    print_welcome()

    while True:
        result = play_round(wins, losses)
        if result == "q":
            break
        elif result == "win":
            wins = wins + 1
        elif result == "loss":
            losses = losses + 1
        print("Next round!\n")


"""Guard function"""
if __name__ == "__main__":
    main()
