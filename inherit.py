
class Vehicle:
    def __init__(self, brand, max_speed, engine, date_of_maufacture, model):
        self.brand = brand
        self.max_speed = max_speed
        self.engine = engine
        self.date_of_maufacture = date_of_maufacture
        self.model = model


class remake(Vehicle):
    def __init__(self, brand, max_speed, engine, date_of_maufacture, model, seat, fuel_type):
        super().__init__(brand, max_speed, engine, date_of_maufacture, model)

        self.seat = seat
        self.fuel_type = fuel_type


car = Vehicle("Tesla", "155mph", "Lithium battery", 2022, "Model Y")

car1 = remake("Tesla", "155mph", "Lithium battery", 2025, "Model Y Juniper", 5, "Electric")


print(car.brand, car.max_speed, car.engine, car.date_of_maufacture, car.model)

print(car1.brand, car1.max_speed, car1.engine, car1.date_of_maufacture, car1.model, car1.seat, car1.fuel_type)
