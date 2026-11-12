class Family_Member:
    def __init__(self, eye_color, height_cm, hair_color):
        self.eye_color = eye_color
        self.height_cm = height_cm
        self.hair_color = hair_color
    def show_traits(self):
        print("Eye Colour:", self.eye_color)
        print("Height (cm):", self.height_cm)
        print("Hair Colour:", self.hair_color)

class Child(Family_Member):
    def __init__(self, name, age, eye_color, height_cm, hair_color):
        self.name = name
        self.age = age
        super().__init__(eye_color, height_cm, hair_color)
    def show_traits(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().show_traits()

    def favourite_hobby(self, hobby):
        print(self.name, "loves", hobby)

child1 = Child("Alice", 10, "Blue", 140, "Blonde")
child2= Child("Sam", 10, "Blue", 140, "Blonde")
child3 = Child("Dylan", 10, "Blue", 140, "Blonde")

child1.show_traits()
child1.favourite_hobby("writing")
child2.show_traits()
child2.favourite_hobby("tennis")
child3.show_traits()
child3.favourite_hobby("badminton")

print("Is Child really a subclass of Family_Member?", issubclass(Child, Family_Member))