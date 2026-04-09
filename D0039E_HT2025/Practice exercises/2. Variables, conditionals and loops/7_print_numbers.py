"""
Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
"""


def main():
    for i in range(0,7):
        if i == 0:
            print(i)
        elif i % 3 == 0:
            continue
        else:
            print(i)


if __name__ == "__main__":
    main()