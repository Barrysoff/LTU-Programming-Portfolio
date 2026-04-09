def celsius_to_fahrenheit(celsius):  # convert Celsius to Fahrenheit
    return 9/5*celsius+32


def fahrenheit_to_celsius(fahrenheit):  # convert Fahrenheit to Celsius
    return 5/9*(fahrenheit-32)


# User choices, conversion direction and starting temperatures

choice = " "
while choice not in "CF":
    choice = input("Enter 'C' to convert Celsius to Fahrenheit, or 'F' to convert Fahrenheit to Celsius: ")
    choice = choice.strip()  # Strip off the spaces at the beginning and at the end
    choice = choice.upper()  # Convert everything to uppercase.

temp_str = input("Enter the temperature: ")
temp = float(temp_str)

# Convert temperatures
if choice == "C":
    converted = celsius_to_fahrenheit(temp)
    print(f"{temp:.1f}°C is {converted:.2f}°F")
else:
    converted = fahrenheit_to_celsius(temp)
    print(f"{temp:.1f}°F is {converted:.2f}°C")