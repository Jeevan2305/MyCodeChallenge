# Function Decorator
def func_decorator(func):
    def wrapper():
        print("Before call")
        func()
        print("After call")
    return wrapper

@func_decorator
def say_hello():
    print("Hello World")
