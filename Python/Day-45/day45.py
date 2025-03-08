import math
from abc import ABC, abstractmethod

# Define an abstract base class for shapes
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Define a Circle class that inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

# Define a Square class that inherits from Shape
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Define a Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

shapes = [Circle(2), Square(3), Rectangle(4, 5)]

# Calculate and print the area of each shape
for shape in shapes:
    print(shape.area())
