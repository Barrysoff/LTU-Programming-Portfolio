"""
Write a Python program to display the astrological sign for a given date of birth.
"""


def main():
    date_str = input("What is your birthdate (mmdd)? ")

    try:
        date = int(date_str)
    except ValueError:
        print("That is not a valid date!")
        return

    if 1222 <= date <= 1231 or 101 <= date <= 119:
        print("You are a Capricorn!")
    elif 120 <= date <= 131 or 201 <= date <= 218:
        print("You are a Aquarius!")
    elif 219 <= date <= 229 or 301 <= date <= 320:
        print("You are a Pisces!")
    elif 321 <= date <= 331 or 401 <= date <= 419:
        print("You are a Aries!")
    elif 420 <= date <= 430 or 501 <= date <= 521:
        print("You are a Taurus!")
    elif 522 <= date <= 531 or 601 <= date <= 620:
        print("You are a Gemini!")
    elif 621 <= date <= 630 or 701 <= date <= 722:
        print("You are a Cancer!")
    elif 723 <= date <= 731 or 801 <= date <= 822:
        print("You are a Leo!")
    elif 823 <= date <= 830 or 901 <= date <= 922:
        print("You are a Virgo!")
    elif 923 <= date <= 931 or 1001 <= date <= 1022:
        print("You are a Libra!")
    elif 1023 <= date <= 1031 or 1101 <= date <= 1121:
        print("You are a Scorpio!")
    elif 1122 <= date <= 1130 or 1201 <= date <= 1221:
        print("You are a Sagittarius!")
    else:
        print("That is not a valid date!")
        return

if __name__ == "__main__":
    main()