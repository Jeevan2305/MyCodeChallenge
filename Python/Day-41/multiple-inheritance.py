#Multiple Inheritance
class Flyable:
    def fly(self):
        print("It can fly")
        
class Swimmable:
    def swim(self):
        print("It can swim")
        
class Duck(Flyable, Swimmable):
    def fly(self):
        print("Duck can fly")
        
    def swim(self):
        print("Duck can swim")

duck = Duck()
duck.fly()
duck.swim()
