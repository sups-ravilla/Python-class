num_str = input("Enter a number: ")

cleaned_num_str = ''.join(filter(str.isdigit, num_str))

if not cleaned_num_str:
    print("No digits found in your input.")
else:
    # Calculate the number of digits
    num_digits = len(cleaned_num_str)
    print(f"The number {num_str} has {num_digits} digits.")