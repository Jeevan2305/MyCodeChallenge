# Create a simple calculator program that can add, subtract, multiply, and divide two integers
def add_integer(a, b):
    return a + b

def subtract_integer(a, b):
    return a - b

def multiply_integer(a, b):
    return a * b

def divide_integer(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b

while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")
    ch = int(input("Enter your choice : "))
    if ch == 0:
        break
    n1 = int(input("Integer 1 : "))
    n2 = int(input("Integer 2 : "))
    if ch == 1:
        print(f"Result : {add_integer(n1, n2)}")
    elif ch == 2:
        print(f"Result : {subtract_integer(n1, n2)}")
    elif ch == 3:
        print(f"Result : {multiply_integer(n1, n2)}")
    elif ch == 4:
        print(f"Result : {divide_integer(n1, n2)}")
    else:
        print("Invalid choice. Please choose a valid option.")
