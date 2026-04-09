# Import the math module

import math

# Create variables

distance_km = 450
fuel_efficiency = 15
fuel_price = 1.20
average_speed = 80

# Calculate travel time

Time = distance_km / average_speed

# Calculate fuel cost

Fuel_needed = distance_km / fuel_efficiency

Fuel_cost = Fuel_needed * fuel_price

# Display the result on screen

print(f"Total distance: {distance_km} km")
print(f"Estimated Travel Time: {math.ceil(Time)} hours")
print("Fuel Needed: %.2f liters" % Fuel_needed)
print("Total Fuel Cost: $%.2f" % Fuel_cost)