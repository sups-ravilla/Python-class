number = int(input("Hello, please enter a number: "))
power = int(input("Please enter the exponent of your number: "))

result = 1

for i in range(power):
    result *= number

print(f"The {number} to the power of {power} is: {result}")