"""
Mandatory assignment 3, Inventory Management System
Author: Mattias Westermark
"""

# Create an Inventory Management System that simulates managing a store or warehouse inventory.
# The system allows the user to track items, update quantities, calculate values, and perform data operations.


inventory = {}


def print_menu():
    """
    Print menu for user to make their choice.
    """

    print("1. Add item to inventory")
    print("2. Update item in inventory")
    print("3. Remove item from inventory")
    print("4. View inventory")
    print("5. Check total value of inventory")
    print("6. Find low stock")
    print("7. Exit")
    return None


def add_item():
    """
    Allow the user to add an item with the following attributes:
        Item Name (String)
        Item ID (Unique Integer)
        Quantity (Integer)
        Price Per Unit (Float)
    """

    while True:
        try:
            item_id = int(input("Enter item ID (unique integer): "))
            if item_id in inventory:
                print("Error: Item ID already exists. Try a different ID.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer for the item ID.")

    while True:
        item_name = input("Enter item name: ").strip()
        if item_name:
            break
        print("Item name cannot be empty!")

    while True:
        try:
            item_quantity = int(input("Enter quantity: "))
            if item_quantity >= 0:
                break
            print("Quantity cannot be negative.")
        except ValueError:
            print("Invalid input! Please enter a valid integer for the quantity.")

    while True:
        try:
            item_price = float(input("Enter price per unit: "))
            if item_price >= 0:
                break
            print("Price cannot be negative.")
        except ValueError:
            print("Invalid input! Please enter a valid number for the price.")

    new_item = {
        "name": item_name,
        "quantity": item_quantity,
        "price": item_price
    }

    inventory[item_id] = new_item

    print(f"Item {item_name} added successfully!")


def update_item():
    """
    Allow the user to update an item’s name, quantity, or price.
    """

    while True:
        if len(inventory) == 0:
            print("Error: there are no items to update.")
            break

        try:
            item_id = int(input("Enter item ID to update: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer for the item ID.")
            continue

        if item_id not in inventory:
            print("Error: Item not found.")
            break

        print("Enter new values (press Enter to keep existing values):")
        new_name = input(f"Current Name: {inventory[item_id]['name']} | New Name: ")
        if new_name == "":
            new_name = inventory[item_id]['name']

        new_quantity = (input(f"Current Quantity: {inventory[item_id]['quantity']} | New Quantity: "))

        if new_quantity == "":
            new_quantity = inventory[item_id]['quantity']

        try:
            new_quantity = int(new_quantity)
        except ValueError:
            print("Invalid input! Enter a valid integer for the quantity.")
            continue
        if new_quantity <= 0:
            print("Quantity cannot be negative.")
            break

        new_price = (input(f"Current Price: {inventory[item_id]['price']} | New Price: "))
        if new_price == "":
            new_price = inventory[item_id]['price']

        try:
            new_price = float(new_price)
        except ValueError:
            print("Invalid input! Please enter a valid number for the price.")
            continue

        inventory[item_id]['name'] = new_name
        inventory[item_id]['quantity'] = new_quantity
        inventory[item_id]['price'] = new_price

        break


def remove_item():
    """
    Remove an item from the inventory using its ID.
    """

    while True:
        if len(inventory) == 0:
            print("Error: there are no items to remove.")
            break

        try:
            item_id = int(input("Enter the ID of the item to remove: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer for the item ID.")
            continue
        if item_id not in inventory:
            print("Error: Item not found.")
            break

        del inventory[item_id]

        print("Item removed successfully!")

        break


def view_inventory():
    """
    Display all items with details such as:
        Name, ID, Quantity, Price, and Total Value (Quantity × Price).
    """

    print("Current Inventory:")

    if inventory == {}:
        print("No items in inventory.")
    else:
        print("-" * 60)
        print(f"{'ID':<6}{'Name':<15}{'Quantity':>10}{'Price':>10}{'Total Value':>15}")
        print("-" * 60)
        for item_id in inventory:
            print(f"{item_id:<6}{inventory[item_id]['name']:<13}{inventory[item_id]['quantity']:9.2f}{inventory[item_id]['price']:14.2f}{inventory[item_id]['quantity'] * inventory[item_id]['price']:10.2f}")
        print("-" * 60)


def check_total_value():
    """
    Calculate the total value of all items in the inventory.
    """

    running_total = 0

    for item_id in inventory:
        running_total += inventory[item_id]['quantity'] * inventory[item_id]['price']

    print(f"Total inventory value: {running_total:.2f}")


def find_low_stock():
    """
    Identify and list items with quantities below a user-defined threshold.
    """

    low_stock = {}

    print("Checking for Low Stock Items")
    while True:
        if len(inventory) == 0:
            print("Error: there are no items in inventory.")
            break

        try:
            threshold = int(input("Enter the low stock threshold: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

        if threshold < 0:
            print("Threshold must be larger or equal to 0.")
            continue

        for item_id in inventory:
            if inventory[item_id]['quantity'] <= threshold:
                low_stock[item_id] = inventory[item_id]

        if len(low_stock) == 0:
            print("No items with low stock.")
        else:
            for item_id in low_stock:
                print(f"- Name: {low_stock[item_id]['name']}, ID: {item_id}, Quantity: {low_stock[item_id]['quantity']}")

        break


def main():
    """
    Print menu and wait for users choice.
    """

    while True:
        print_menu()

        choice = input("Make a choice, 1-7: ").strip()

        if choice == "7":
            print("Goodbye!")
            break
        elif choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            view_inventory()
        elif choice == "5":
            check_total_value()
        elif choice == "6":
            find_low_stock()
        else:
            print("Invalid choice. Please try again!")
        print()


if __name__ == "__main__":
    main()
