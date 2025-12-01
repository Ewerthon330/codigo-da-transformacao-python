class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_information(self):
        return f"{self.brand} {self.model}"
    
my_car = Car("Honda", "HRV")
print(my_car.display_information())