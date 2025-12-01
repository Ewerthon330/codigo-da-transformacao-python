class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Carro: {self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_autonomy):
        super().__init__(brand, model)
        self.battery_autonomy = battery_autonomy

    def __str__(self):
        return f"Carro elétrico: {self.brand} {self.model}, Bateria: {self.battery_autonomy}"


car1 = Car("Honda", "Civic")
car2 = ElectricCar("Tesla", "Model 3", "400km")

print(car1)
print(car2)
