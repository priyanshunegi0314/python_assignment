class Vehicle:
    def calculate_fare(self, km):
        pass

class Auto(Vehicle):
    def calculate_fare(self, km):
        return km * 10

class Bike(Vehicle):
    def calculate_fare(self, km):
        return km * 8

class Sedan(Vehicle):
    def calculate_fare(self, km):
        return km * 15

vehicles = [Auto(), Bike(), Sedan()]

for v in vehicles:
    print(v.__class__.__name__, "Fare:", v.calculate_fare(10))
