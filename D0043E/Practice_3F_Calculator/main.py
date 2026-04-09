"""
Define functions for each operation
"""


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    result = 0
    negative = False

    if y < 0:
        y = -y
        negative = True

    for i in range(y):
        result = result + x

    if negative:
        return -result

    return result


def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y


# User inputs

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
oper = input("Enter the operation (+, -, *, /): ")

if oper == "+":
    result = add(num1, num2)
elif oper == "-":
    result = subtract(num1, num2)
elif oper == "*":
    result = multiply(num1, num2)
elif oper == "/":
    result = divide(num1, num2)
else:
    result = "Invalid operation!"

print(f"The result of {num1} {oper} {num2} is {result}.")