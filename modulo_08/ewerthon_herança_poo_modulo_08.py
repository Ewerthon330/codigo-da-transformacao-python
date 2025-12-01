class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class EletricCar(Car):

    def __init__(self, brand, model, battery_autonomy):
        super().__init__(brand, model)
        self.battery_autonomy = battery_autonomy

car = EletricCar("Honda", "Civic", "500km")
print(car.brand, car.model, car.battery_autonomy)