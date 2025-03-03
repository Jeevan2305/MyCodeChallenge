# Hierarchical Inheritance
class Vehicle:
    tyre = 0
    reverse = False

class Car(Vehicle):
    tyre = 4
    reverse = True

class Bike(Vehicle):
    tyre = 2

car = Car()
bike = Bike()

print(car.tyre)
print(car.reverse)
print(bike.tyre)
print(bike.reverse)
