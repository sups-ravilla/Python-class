class fruit:
    def __init__(self, name, color, price, taste, count,):
        self.name = name
        self.color = color
        self.price=price
        self.taste=taste
        self.count = count
    def intro(self):
        print("Hello this fruit is a", self.name)
        print("The color of this fruit is", self.color)
        print("The price of this fruit is", self.price)
        print("The taste of this fruit is", self.taste)
        print("The count of this fruit is", self.count)
ob= fruit("Apple", "Red", "1.00", "Sweet", 4)
total_cost = ob.price * ob.count            
ob.intro()
print("The total cost of the fruits is", total_cost)
