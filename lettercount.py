string = input("Please enter your name:")

char = input("Please enter a character of your name: ")

i = 0
count = 0

while (i <len(string)):

    if (string[i] == char):
        count = count + 1
    i = i + 1

print("The total number of times ", char, "Has occured = " ,count)   
print("Thank you for using this program.Have a nice day.") 