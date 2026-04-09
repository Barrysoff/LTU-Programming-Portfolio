def calculator():
    while True:
        try:
            # Ask user for first number and validate or exit
            num_1_str = input("Enter the first number: ")
            if num_1_str.lower() == "exit":
                print("Goodbye!")
                break

            num_1 = float(num_1_str)

            # Ask user for second number and validate or exit
            num_2_str = input("Enter the second number: ")
            if num_2_str.lower() == "exit":
                print("Goodbye!")
                break

            num_2 = float(num_2_str)

            # Ask user for operator or exit
            oper_str = input("Choose an operation (+, -, *, /): ")
            if oper_str.lower() == "exit":
                print("Goodbye!")
                break

            # Perform the calculations
            if oper_str == "+":
                result = num_1 + num_2
            elif oper_str == "-":
                result = num_1 - num_2
            elif oper_str == "*":
                result = num_1 * num_2
            elif oper_str == "/":
                result = num_1 / num_2
            else:
                print("Invalid operation! Please choose +, -, *, or /.")
                continue

            print(f"Result: {result}")

        # Error handling
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except ZeroDivisionError:
            print("Cannot divide by zero!")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            print("Calculation complete.\n")


def main():
    calculator()


"""Guard function"""
if __name__ == "__main__":
    main()