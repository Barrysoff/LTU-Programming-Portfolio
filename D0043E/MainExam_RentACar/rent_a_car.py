"""
Main Exam Programming Problem - LTU Rent a Car
Author: Mattias Westermark

Note: Gemini has been used as a sounding board
in accordance with the allowed aids policy.
"""


# Global data storage


cars = {}
"""
Key: registration number (string, for example "CYW426")
Value: another dictionary with:
    "model" - make and model (string, e.g. "BMW 330i xDrive")
    "status" - "Available" or "Rented"
"""


rentals = []
"""
Use a list of dictionaries to store rental records. Each rental record should contain:

    "reg" - registration number (string)
    "renter" - renter's full name (string)
    "start_hour" - pickup hour as an integer (0-23)
    "end_hour" - return hour as an integer (0-23), or None if not yet returned
    "hours" - duration in hours (number), or None if not yet returned
    "cost" - rental cost in SEK (number), or None if not yet returned
"""


rate = 120  # rate is 120 SEK/hour


def add_car():  # Add Car to Fleet
    """
    Asks the user for a registration number and make and model of the car
    Input validation:
        Registration number (string)
            must be at least 4 characters long
            must not contain spaces
            must be unique (not already in the cars dictionary)
        Make and model (string)
            must not be empty
    """

    # Input and Input Validation

    reg = input("Enter registration number: ").strip()

    if len(reg) < 4:
        print("Error: Registration number must be at least 4 characters long.\n")
        return

    if " " in reg:
        print("Error: Registration number cannot contain spaces.\n")
        return

    if reg in cars:
        print("Error: Registration number already exists.\n")
        return

    model = input("Enter make and model: ").strip()

    if model == "":
        print("Error: Make and model cannot be empty.\n")
        return

    # Populate global dictionary

    cars[reg] = {"model": model, "status": "Available"}

    # User feedback

    print(f"{model} with registration number {reg} was added to car fleet.\n")


def rent_car():  # Rent a Car
    """
    Asks the user for registration number, pickup hour and renters full name
    Input validation:
        Registration number (string)
            at least 4 characters, no spaces
            must exist in cars{}
            status must be "Available" (not already rented)
        Pickup hour:
            must be an integer
            must be between 0 and 23 (inclusive)
        Renter name:
            must not be empty
    """

    # Input and Input Validation

    reg = input("Enter car's registration number: ").strip()

    if len(reg) < 4:
        print("Error: Registration number must be at least 4 characters long.\n")
        return

    if " " in reg:
        print("Error: Registration number cannot contain spaces.\n")
        return

    if reg not in cars:
        print("Error: Car not found.\n")
        return

    if cars[reg]['status'] == "Rented":
        print("Error: Car is not available.\n")
        return

    start_hour_str = input("Enter pickup hour (0-23): ").strip()

    try:
        start_hour = int(start_hour_str)
    except ValueError:
        print("Error: Invalid hour! Please enter an integer between 0 and 23.\n")
        return
    if start_hour < 0 or start_hour > 23:
        print("Error: Invalid hour! Please enter an integer between 0 and 23.\n")
        return

    renter = input("Enter renter's name: ")

    if renter == "":
        print("Error: Renter name cannot be empty.\n")
        return

    # Update global dictionary and list

    cars[reg]['status'] = "Rented"

    rentals.append({"reg": reg, "renter": renter, "start_hour": start_hour, "end_hour": None, "hours": None, "cost": None})

    # User feedback

    print(f"Car with registration number {reg} was rented by {renter} at {start_hour}.\n")


def return_car():  # Return a Car
    """
    Asks the user for registration and return hour
    Input validation:
        Registration number (string)
            at least 4 characters, no spaces
            must exist in cars{}
            status must be "Rented" (car must already be rented)
        Return hour:
            must be an integer
            must be between 0 and 23
            must be greater than the pickup hour for that active car's rental
    """

    active_rental = None  # Place holder for car to be returned

    # Input and Input Validation

    reg = input("Enter registration number: ").strip()

    if len(reg) < 4:
        print("Error: Registration number must be at least 4 characters long.\n")
        return

    if " " in reg:
        print("Error: Registration number cannot contain spaces.\n")
        return

    if reg not in cars:
        print("Error: Car not found.\n")
        return

    if cars[reg]['status'] == "Available":
        print("Error: Car is not rented.\n")
        return

    end_hour_str = input("Enter return hour (0-23): ").strip()

    try:
        end_hour = int(end_hour_str)
    except ValueError:
        print("Error: Invalid hour! Please enter an integer between 0 and 23.\n")
        return
    if end_hour < 0 or end_hour > 23:
        print("Error: Invalid hour! Please enter an integer between 0 and 23.\n")
        return

    # Control functions to see if a car can be returned

    for rental in rentals:
        if rental['reg'] == reg and rental['end_hour'] is None:
            active_rental = rental
            break

    if active_rental['start_hour'] >= end_hour:
        print("Error: Return hour must be later than pickup hour.\n")
        return
    else:
        active_rental['end_hour'] = end_hour

    active_rental['hours'] = active_rental['end_hour'] - active_rental['start_hour']
    active_rental['cost'] = active_rental['hours'] * rate

    cars[reg]['status'] = "Available"

    # Print Receipt

    print("=" * 34)
    print("LTU Rent-a-Car")
    print("=" * 34)
    print(f"Name: {active_rental['renter']}")
    print(f"Car: {cars[reg]['model']} ({active_rental['reg']})")
    print(f"Time: {active_rental['start_hour']}-{active_rental['end_hour']} ({active_rental['hours']} hours)")
    print(f"Total cost: {active_rental['cost']} SEK\n")


def view_fleet():  # View Car Fleet
    """
    Print a summary of all cars in the fleet
    """

    available = 0

    if len(cars) == 0:
        print("No cars in fleet.\n")
        return

    car_list = list(cars)
    car_list_sorted = bubble_sort(car_list)

    print("LTU Rent-a-Car car fleet:")
    print("Fleet:")
    print(f"{'Model':<25}{'Registration':<20}{'Status':<15}")
    for car in car_list_sorted:
        print(f"{cars[car]['model']:<25}{car:<20}{cars[car]['status']:<15}")
        if cars[car]['status'] == "Available":
            available += 1
    print(f"Total number of cars: {len(cars)}")
    print(f"Total number of available cars: {available}\n")


def view_rentals():  # View Rental Summary
    """
    Print a summary of all rentals (both completed and not yet returned).
    """

    temp_list = rentals[:]
    names = []
    revenue = 0

    if len(rentals) == 0:
        print("No rentals for today.\n")
        return

    for rental in rentals:
        names.append(rental['renter'])

    names_sorted = bubble_sort(names)

    print("LTU Rent-a-Car rental summary:")
    print("Rentals:")
    print(f"{'Name':<25}{'Registration':<15}{'Pickup':<8}{'Return':<8}{'Cost'}")

    # The routine for sorting and printing rentals was difficult to get together,
    # Gemini was patient explaining a strategy with nested loops as well has
    # handling printouts when end_hour and cost = None.

    for name in names_sorted:
        for rental in temp_list:
            if rental["renter"] == name:
                end_str = rental['end_hour']
                if end_str is None:
                    end_str = ""
                cost_str = rental['cost']
                if cost_str is None:
                    cost_str = ""
                else:
                    revenue += rental['cost']
                    cost_str = f"{int(cost_str)} SEK"
                print(f"{name:<25}{rental['reg']:<15}{rental['start_hour']:<8}{end_str:<8}{cost_str}")
                temp_list.remove(rental)  # Handle multiple renters with identical names
                break
    print(f"Total number of rentals: {len(rentals)}")
    print(f"Total revenue: {int(revenue)} SEK")


def bubble_sort(list_to_sort):  # Sorts a list of cars
    """
    Sorts a list of cars, either by registration number or by renter,
    in ascending order using the buble sort algorithm.
    Returns the sorted list.
    """
    result = list_to_sort[:]
    n = len(result)

    # Outer loop
    for i in range(0, n):
        # Inner loop
        for j in range(0, n - i - 1):
            # Compare ajacent elements
            if result[j] > result[j + 1]:
                # Traditional swap
                temp = result[j]
                result[j] = result[j + 1]
                result[j + 1] = temp

    return result


def main():
    """
    Prints menu and waits for user input.
    Input validation:
        Option (string)
            must be numbers from 1 to 5 or q.
    """
    while True:
        print("# LTU Rent-a-Car")
        print("1. Add car to fleet")
        print("2. Rent a car")
        print("3. Return a car")
        print("4. View car fleet")
        print("5. View rental summary")
        print("q. Exit program")
        option = input("Enter your option: ").strip()

        if option not in ["1", "2", "3", "4", "5", "q"]:
            print("Invalid option! Please choose 1-5 or q.\n")
        elif option == "q":
            print("Goodbye!")
            break
        elif option == "1":
            add_car()
        elif option == "2":
            rent_car()
        elif option == "3":
            return_car()
        elif option == "4":
            view_fleet()
        elif option == "5":
            view_rentals()


if __name__ == "__main__":
    main()
