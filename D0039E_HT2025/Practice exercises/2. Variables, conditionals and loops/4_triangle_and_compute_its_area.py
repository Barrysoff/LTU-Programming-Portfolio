"""
Write a Python program that will accept the base and height
 of a triangle and compute its area.
"""


def main():
    try:
        base = float(input("What is the base of the triangle in mm? "))
        height = float(input("What is the height of the triangle in mm? "))
    except ValueError:
        print("That is not a valid measurement!")
        return

    area = base * height / 2

    print(f"The area of the triangle is {area} mm^2.")


if __name__ == "__main__":
    main()