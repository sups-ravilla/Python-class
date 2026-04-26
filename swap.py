print("Hello there. please enter three numbers for me to swap")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

random_swap = input(str("Do you want me to randomly swap the numbers? (yes/no)"))
if random_swap == 'yes' :
  num1, num2, num3 = num2, num3, num1
  print(f"The numbers after swapping are: num1={num1}, num2={num2}, num3={num3}")
else:
  print("Thank you for using this code. Have a nice day")