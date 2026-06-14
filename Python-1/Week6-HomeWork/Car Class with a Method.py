class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    def describe(self):
        print(f"This is a {self.color} {self.brand} {self.model}")
c1 = Car("Toyota", "Camry", "red")
c1.describe()