class Parrot:
    species = "bird"

    def __init__(self, name, age, origin):
        self.name = name
        self.age = age
        self.origin = origin
Robert = Parrot("Robert", 10, "Amazon Rainforest")
Jamie = Parrot("Jamie", 45, "Brazil")
Jeff = Parrot("Jeff", 110, "Peru")

print("============PARROTS AT THE BIRD HOUSE============")
print("")
print("Robert is a {}".format(Robert.species))
print("Jamie is a {}".format(Jamie.species))
print("Jeff is a {}".format(Jeff.species))
print("")
print("{} is {} years old and is abducted from the {}".format(Robert.name, Robert.age, Robert.origin))
print("{} is {} years old and is abducted from {}".format(Jamie.name, Jamie.age, Jamie.origin))
print("{} is {} years old and is abducted from {}".format(Jeff.name, Jeff.age, Jeff.origin))