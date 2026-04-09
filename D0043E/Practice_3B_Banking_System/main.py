# Definition of a function to check input variables

def get_number_input(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            value = int(value)
            return value
        else:
            print("Invalid choice! Please select an option between 1 and 4.")


# Declare starting variables
balance = 1000

# Prompt user for option
while True:
    # Create menu interface
    print("Welcome to Simple Bank!")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    num = get_number_input("\nChoose an option: ")

    # Option 1: check balance
    if num == 1:
        print(f"Your current balance is: ${balance}")

    # Option 2: deposit money
    elif num == 2:
        amount = int(input("Enter the amount to deposit: "))
        balance = balance + amount
        print(f"You have successfully deposited ${amount}. Your new balance is: ${balance}")

    # Option 3: withdraw money
    elif num == 3:
        amount = int(input("Enter the amount to withdraw: "))
        if amount > balance:
            print(f"Insufficient balance! You only have ${balance} in your account.")
        else:
            balance = balance - amount
            print(f"You have successfully withdrawn ${amount}. Your new balance is: ${balance}")

    # Option 4: exit
    elif num == 4:
        print("Thank you for using Simple Bank! Goodbye!")
        break
    else:
        print("Invalid choice! Please select an option between 1 and 4.")
else:
    print("Invalid choice! Please select an option between 1 and 4.")