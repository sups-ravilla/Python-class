import math

def my_function():
  r = float(input("What number would you like to input to solve the circumference for your circle: "))
  circumference = 2 * math.pi * r
  print(f"The circumference of the circle with radius {r} is: {circumference}")

my_function()