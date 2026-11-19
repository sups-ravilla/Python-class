class Computer:

    def __init__(self):
        self.__maxprice = "£900.00"

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = "£1000.00"
c.sell()

c.setMaxPrice("£1000.00")
c.sell()

voucher = str(input("Do you have a voucher or discount code you can use? (Y/N)"))
if voucher == "y" or voucher == "Y":
    discount=int(input("Please enter the discount code: "))
    if discount == 131879:
        print("Your Voucher has been verified please pay the updated ammount of £800.00")
        c.setMaxPrice("£800.00")
        c.sell()
    else:
        print("Error please use another code. If you just wnat money then we'll know😄.")
else:
    print("No worries, please pay the full ammount of £900.00")

print("Thank you for shopping with us. Please come again.")