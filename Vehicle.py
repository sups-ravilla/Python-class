class Vehicle:
    def __init__(self, max_speed, mileage ,model , color , capacity ,make , fuel_type):
        self.max_speed = max_speed
        self.mileage = mileage
        self.model = model
        self.color = color
        self.capacity = capacity
        self.make = make
        self.fuel_type = fuel_type
BYD_Sealion_U = Vehicle(100, 300000, "Sealion U", "Blue", 5, "BYD", "Hybrid")
print("This all the specs of a BYD Sealion U:", BYD_Sealion_U.max_speed, BYD_Sealion_U.mileage, BYD_Sealion_U.model, BYD_Sealion_U.color, BYD_Sealion_U.capacity, BYD_Sealion_U.make, BYD_Sealion_U.fuel_type)        