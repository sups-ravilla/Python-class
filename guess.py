import random
playing = True
number = str(random.randint(0, 9))

print("Step right up, step right up and try your luck with this guessing game! If you guess right you win it all!")
print("This only and only ends when you guess right at last once so try your luck and win it all!")

while playing:
  guess = input("Give me your best shot! \n")
  if number == guess:
    print("You have guessed correctly!")
    print("The number was",number)
    break

  else:
    print("Sorry, that's not it. Try again!")