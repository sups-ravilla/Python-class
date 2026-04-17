print("Hello,this program is an ASCII Value Checker")

print("=" * 40)

 

char = input(" Please enter a single letter or single digit number: ")

 
# Validate input

if type(char) is str and int and len(char) == 1:
        


    ascii_val = ord(char)

    

    # Display results

    print(f"Character: '{char}'")

    print(f"ASCII Value: {ascii_val}")

    

    # Identify type

    print("Character Type: ", end="")

    if ascii_val >= 65 and ascii_val <= 90:

        print("Uppercase Letter")

    elif ascii_val >= 97 and ascii_val <= 122:

        print("Lowercase Letter")

    elif ascii_val >= 48 and ascii_val <= 57:

        print("Digit")

    elif ascii_val == 32:

        print("Space")

    else:

        print("Special Character")

else:

    print("\nError: Please enter exactly ONE character!")