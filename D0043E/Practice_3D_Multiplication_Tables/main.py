# Generating the multiplication table from 1 to 10
for row in range(1, 11):  # Outer loop for numbers 1 to 10, the rows
    for col in range(1, 11):  # Inner loop for numbers 1 to 10, the cols
        print(f"{row * col: 3d}", end=" ")
    print()  # Move to the next line after printing a row