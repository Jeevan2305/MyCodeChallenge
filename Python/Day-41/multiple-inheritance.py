#Multiple Inheritance
class Flyable:
    def fly(self):
        print("Fly")
        
class Swimmable:
    def swim(self):
        print("Swim")
        
class Duck(Flyable, Swimmable):
    def fly(self):
        print("Duck can fly")
        
    def swim(self):
        print("Duck can swim")

duck = Duck()
duck.fly()
duck.swim()
