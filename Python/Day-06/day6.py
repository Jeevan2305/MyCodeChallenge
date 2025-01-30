# Simple Function
# Define and call a simple function greet_user which takes name as a parameter. The function should print 'Hello, name' to the console.
def greet_user(name):
    print(f'Hello, {name}')

greet_user('Jeevan')

# Default and Keyword Arguments
# Update the greet_user function by adding a default value 'Guest' for the name parameter. When the function is called without an argument it should print 'Hello, Guest' to the console.
def greet_user(name = 'Guest'):
    print(f'Hello, {name}')

greet_user()

# Function with Return Values
# Write a function that calculates and returns the area of a rectangle. The function should take length and breadth as the arguments.
def area_of_rect(len, bre):
    return len * bre

print(area_of_rect(10, 20))

# Variable Scope
# To understand the difference between local and global variables, follow these steps:
# 1. Define a global variable and print its value.
# 2. Write a function and assign a new value to the same varible inside the function and then print it.
# 3. Print the variable again outside the function again to observe that its value didn't change.
# 4. Write another function that access the global variable using the global keyword and then update its value.
# 5. Print the variable again outside the function. Verify that it's value now got updated.

x = 10

def var_x():
    x = 20
    print(x)

print(x)
var_x()


y = 2
print(y)

def var_y():
    global y
    y = 4

var_y()
print(y)
