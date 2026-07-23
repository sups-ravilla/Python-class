try:
    num1, num2 = eval(input("Enter 2 numbers separated by a comma: "))
    result = num1 / num2
    print("The result is", result)    


except ZeroDivisionError:
    print("You cannot divide by zero")

except SyntaxError:
    print("You must have a comma separating the 2 numbers")

except:
    print("Wrong input")

else:
    print("There were no errors in your input.Good Job")

finally:
    print("This line of code will always run")