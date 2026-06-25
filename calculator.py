def add(P, Q):

    return P + Q
def subtract(P, Q):

    return P - Q
def multiply(P, Q):

    return P * Q
def divide(P, Q):

    return P / Q


print("Please select the operation that you wish to select.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter the choice of operation that you wnat to use(1/2/3/4)")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':             
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Please try again and select either option 1, 2, 3 or 4 as this is an invalid inpuut.")
 
print("Thank you for using the calculator.I hope your operation was succesful")
