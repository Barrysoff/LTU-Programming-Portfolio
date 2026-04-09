"""
Write a Python program that calculates the area of a circle
based on the radius given as a variable.
"""

import math


def main():
    radius = float(input("Enter a radius: "))
    if radius < 0:
        print("The area of a circle cannot be less than or equal to zero.")
        return
    else:
        area = math.pi * (radius ** 2)
        print("The area of the circle is", area)


if __name__ == '__main__':
    main()