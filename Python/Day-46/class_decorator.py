# Class Decorator
def cls_decorator(cls):
    def greet(self):
        return f"Hello from {self.__class__.__name__}"
    cls.greet = greet
    return cls
    
@cls_decorator
class Person:
    def __init__(self, name):
        self.name = name
        
person = Person("A")
print(person.greet())
