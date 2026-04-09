# Import the math module
import math

# Create variables
str_distance_km = input()
float_distance_km = float(str_distance_km)
int_distance_km = int(str_distance_km)

str_fuel_effiency = input()
float_fuel_effiency = float(str_fuel_effiency)

str_fuel_price = input()
float_fuel_price = float(str_fuel_price)

str_average_speed = input()
float_average_speed = float(str_average_speed)

float_fuel_needed = (float_distance_km / float_fuel_effiency)

# Calculate BMI


def calculate_travel_time(float_distance_km, float_average_speed):
    travel_time = math.ceil(float_distance_km / float_average_speed)
    print("Estimated Travel Time:", travel_time, "hours")


def calculate_fuel_needed(float_distance_km, float_fuel_effiency):
    fuel_needed = (float_distance_km / float_fuel_effiency)
    print(f"Fuel Needed: {fuel_needed:.2f} liters")


def calculate_fuel_cost(fuel_needed, float_fuel_price):
    fuel_cost = (fuel_needed * float_fuel_price)
    print(f"Total Fuel Cost: ${fuel_cost:.2f}")


# Display the result on screen

print("Total Distance:", int_distance_km, "km")

calculate_travel_time(float_distance_km, float_average_speed)

calculate_fuel_needed(float_distance_km, float_fuel_effiency)

calculate_fuel_cost(float_fuel_needed, float_fuel_price)