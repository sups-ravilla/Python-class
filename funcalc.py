import math
import random

print("=== Random Fun Calculator ===")


lucky = random.randint(1, 100)
print("Your lucky number is:", lucky)

activities = ["Walk", "Read", "Code", "Listen to music", "Bake cookies"]
print("Try this:", random.choice(activities))


print("\nGuessing Game!")
secret = random.randint(1, 10)
tries = 0

while True:
    try:
        guess = int(input("Guess a number (1-10): "))
        tries += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("Correct! Attempts:", tries)
            break

    except ValueError:
        print("Enter a number!")

# Math examples
print("\nMath Module:")

number = 4.3
print("The number is:", number)
print("Ceiling:", math.ceil(number))
print("Floor:", math.floor(number))
print("Copy sign:", math.copysign(5, -1))
print("Absolute value:", math.fabs(-7.5))
print("GCD:", math.gcd(24, 36))

print("\nThanks for using the calculator!")