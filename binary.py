n = float(input("Please enter a number with a decimal"))
precision = 10
res = "0."

fraction = n - int(n)

if fraction == 0:
    res = "0.0"
else:
    for i in range(precision):
        if fraction <= 0:
            break
            
      
        for j in range(1):
            fraction *= 2
            bit = int(fraction)
            res += str(bit)
            fraction -= bit

print(f"The binary representation of {n} is approximately: {res}")