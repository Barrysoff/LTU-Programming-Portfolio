"""
Practice Exam Programming Problem - LTU Airport Flight Manager
Author: Mattias Westermark
"""


flights = {}


def add_flight():
    """
    Asks the user for a flight number, destination and status to add to the flight manager.
    Input validation:
        Flight number (string)
            must be at least 3 characters long
            cannot already exist in the dictionary
        Destination (string)
            cannot be empty
        Status (string)
            must be exactly one of: Scheduled, Boarding, Departed
    """

    flight_number = input("Enter flight number: ").strip()

    if len(flight_number) < 3:
        print("Error: Flight number must be at least 3 characters long.\n")
        return

    if flight_number in flights:
        print("Error: Flight number already exists.\n")
        return

    destination = input("Enter destination: ").strip()
    if destination == "":
        print("Error: Destination cannot be empty.\n")
        return

    status = input("Enter status (Scheduled/Boarding/Departed): ").strip()
    if status not in ["Scheduled", "Boarding", "Departed"]:
        print("Error: Invalid status! Choose Scheduled, Boarding, or Departed.\n")
        return

    flights[flight_number] = {"destination": destination, "status": status}

    print(f"Flight {flight_number} to {destination} added successfully!\n")


def update_status():
    """
    Asks the user for a flight number to update
    Input validation:
        Flight number (string)
            must exist in dictionary
        Status (string)
            must be exactly one of: Scheduled, Boarding, Departed or empty
    """

    flight = input("Enter flight number: ").strip()
    if flight not in flights:
        print("Error: Flight not found.\n")
        return

    print(f"Current status: {flights[flight]['status']}\n")

    new_status = input("Enter new status (Scheduled/Boarding/Departed) or press Enter to keep the current status: ").strip()

    if new_status == "":
        pass
    elif new_status not in ["Scheduled", "Boarding", "Departed"]:
        print("Error: Invalid status! Choose Scheduled, Boarding, or Departed.\n")
        return
    else:
        flights[flight]['status'] = new_status

    print(f"Flight {flight} status updated successfully!\n")


def remove_flight():
    """
    Asks the user for a flight number to remove.
    Input validation:
        Flight number (string)
            must exist in the dictionary
    """

    flight = input("Enter flight number to remove: ").strip()
    if flight not in flights:
        print("Error: Flight not found.\n")
        return
    else:
        del flights[flight]

    print(f"Flight {flight} removed successfully!\n")


def view_flights():
    """
    Shows the current flights listed in the flight manager, sorted alphabetically
    Shows a special message if there are no flights.
    """

    if len(flights) == 0:
        print("No flights registered.\n")
        return

    flight_list = list(flights)

    flight_list_sorted = bubble_sort(flight_list)

    print("Current flights:")
    print("-" * 60)
    print(f"{'Flight':<9}{'Destination':<20}{'Status':<15}")
    print("-" * 60)
    for flight_number in flight_list_sorted:
        print(f"{flight_number:<9}{flights[flight_number]['destination']:<20}{flights[flight_number]['status']:<15}")
    print("-" * 60, "\n")


def find_by_status():
    """
    Asks the user for a status. Show flights with this status, sorted alphabetically.
    Input validation:
        Status (string)
            must be exactly one of: Scheduled, Boarding, Departed
    """

    matching_flights = []

    flight_status = input("Enter status to search for (Scheduled/Boarding/Departed): ").strip()

    if flight_status not in ["Scheduled", "Boarding", "Departed"]:
        print("Error: Invalid status! Choose Scheduled, Boarding, or Departed.\n")
        return

    for flight in flights:
        if flights[flight]['status'] == flight_status:
            matching_flights.append(flight)

    if len(matching_flights) == 0:
        print(f"No flights found with status {flight_status}.\n")
        return

    flight_list_sorted = bubble_sort(matching_flights)

    print(f"Flights with status {flight_status}:")
    print("-" * 60)
    print(f"{'Flight':<9}{'Destination':<20}")
    print("-" * 60)
    for flight_number in flight_list_sorted:
        print(f"{flight_number:<9}{flights[flight_number]['destination']:<20}")
    print("-" * 60, "\n")


def count_flights():
    """
    No user input. Shows the total number of flights in the flight manager
    """

    print(f"Total flights registered: {len(flights)}\n")


def bubble_sort(flight_list):
    """
    Sorts a list of flight numbers (strings)
    in ascending order using the bubble sort algorithm.
    Returns the sorted list.
    """

    result = flight_list[:]
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
    Prints menu and waits for user to make a choice.
    Input validation:
        Option (string)
            must be numbers from 1 to 6 or q
    """

    while True:
        print("# LTU Airport Flight Manager")
        print("1. Register a new flight")
        print("2. Update flight status")
        print("3. Remove a flight")
        print("4. View all flights")
        print("5. Find flights by status")
        print("6. Count total flights")
        print("q. Exit program")
        option = input("Enter your option: ").strip()

        if option not in ["1", "2", "3", "4", "5", "6", "q"]:
            print("Invalid option! Please choose 1-6 or q.\n")
        elif option == "q":
            print("Goodbye!")
            break
        elif option == "1":
            add_flight()
        elif option == "2":
            update_status()
        elif option == "3":
            remove_flight()
        elif option == "4":
            view_flights()
        elif option == "5":
            find_by_status()
        elif option == "6":
            count_flights()


if __name__ == "__main__":
    main()
