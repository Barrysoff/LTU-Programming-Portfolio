# Variables for rectangle
str_length = input()
float_length = float(str_length)

str_width = input()
float_width = float(str_width)

# Variables for circle
str_radius = input()
float_radius = float(str_radius)
PI = 3.14

# Calculate and print the rectangle's area


def rectangle_area(float_length, float_width):
    area = float_length * float_width
    print("The area of the rectangle is:", area)


rectangle_area(float_length, float_width)

# Calculate and print the circle's area


def circle_area(float_radius):
    area = PI * float_radius ** 2
    print("The area of the circle is:", area)


circle_area(float_radius)