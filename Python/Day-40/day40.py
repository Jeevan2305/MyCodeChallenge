# Create a class hierarchy for different shapes (circle, square, triangle).
class Shape():
    def perimeter(self):
        print("Perimeter is not implemented")
    def area(self):
        print("Area is not implemented")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return int(2 * (22/7) * self.radius)

    def area(self):
        return int(math.pi * (22/7) * self.radius)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

rad = float(input("Enter Radius : "))
cir = Circle(rad)

print(f"Perimeter of Circle : {cir.perimeter()}")
print(f"Area of Circle : {cir.perimeter()}")

s = int(input("Enter Side : "))
sq = Square(s)

print(f"Perimeter of Square : {sq.perimeter()}")
print(f"Area of Square : {sq.area()}")

leng = int(input("Enter Length : "))
wid = int(input("Enter Width : "))
rect = Rectangle(leng, wid)
print(f"Perimeter of Rectangle : {rect.perimeter()}")
print(f"Area of Rectangle : {rect.area()}")

t1 = int(input("Enter Side 1 : "))
t2 = int(input("Enter Side 2 : "))
t3 = int(input("Enter Side 3 : "))
tri = Triangle(t1, t2, t3)
print(f"Perimeter of Trinangle: {tri.perimeter()}")
print(f"Area of Triangle : {tri.area()}")
