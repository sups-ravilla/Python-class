valid = False
while not valid:
    try:
        n=int(input("Enter a Number"))

        while n%2==0:

            print("You do realise that this is the longest bye you'll probably see?")
        valid = True
    except ValueError:
      print("Invalid")