n = int(input("Please enter a number:"))

print("Numbers from {0} to {1} are :".format(n,1))

for i in range(n, 0, -1):
    print(i, end=" ")