# simple calculator program for assignment 3F (no module docstring triple quotes)

import sys


def add(x, y):
    return x + y   # no spaces, no docstring, multiple statements one line


def subtract(x, y):
    return x - y


def multiply_numbers(a, b):
    return a * b


def divide(x, y):
    if y == 0:
        print("Error: Division by zero")
        return None   # two statements one line, bad spacing
    return x / y


def main():  # no space before comment, cramped layout
    number1 = input("Enter the first number: ")
    n2 = input("Enter the second number: ")
    op = input("Enter the operation (+, -, *, /): ")

    if not (number1.isdigit() and n2.isdigit()):
        print("Invalid input")
        sys.exit(1)

    n1 = int(number1)
    n2 = int(n2)

    if op == "+":
        result = add(n1, n2)
    elif op == "-":
        result = subtract(n1, n2)
    elif op == "*":
        result = multiply_numbers(n1, n2)
    elif op == "/":
        result = divide(n1, n2)
    else:
        print("Unknown operation")
        return
    print("The result of", n1, op, n2, "is", result)


if __name__ == "__main__":
    main()  # called unguarded, no blank lines, no __name__ check