class Pet:
    species = "Dog"
    breed = "Labrador"

    def __init__(self, name, age, food, fav_toy, activity, fur):
        self.name = name
        self.age = age
        self.food = food
        self.fav_toy = fav_toy
        self.activity = activity
        self.fur = fur
Charlie = Pet("Charlie", 5, "Chicken pellets", "Ball", "Swimming", "Black")
print("============MY DOG CHARLIE============")        
print("{} is a {} and is {} years old.".format(Charlie.name, Charlie.breed, Charlie.age))
print("{} loves to eat {} and his favourite toy is a {}.".format(Charlie.name, Charlie.food, Charlie.fav_toy))
print("{} has {} fur and enjoys {}.".format(Charlie.name, Charlie.fur, Charlie.activity))
