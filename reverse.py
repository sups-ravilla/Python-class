string = str(input("Please enter a word:"))

string2 = ('')
for i in string:
    string2 = i + string2

print("/nThe original word is:", string)
print("The reversed word is:", string2)