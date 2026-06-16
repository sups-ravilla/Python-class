def mirrored_triangle(rows):
    for i in range(1, rows + 1):
        # Print spaces first, then print the asterisks
        spaces = " " * (rows - i)
        stars = "*" * i
        print(spaces + stars)

# Ask the user for input and convert it to an integer
try:
    num_rows = int(input("Enter the number of rows for the triangle: "))
    if num_rows > 0:
        mirrored_triangle(num_rows)
    else:
        print("Please enter a number greater than 0.")
except ValueError:
    print("Invalid input! Please enter a valid whole number.")