# 1. Write a program to convert temperature from Celsius to Fahrenheit. 
cel = int(input("Enter celsius: "))

def cel_to_farh(cel):
    farh = float((cel * 9)/5 + 32)
    return farh

print(cel_to_farh(cel))

# 2. Write a program to convert temperature from Fahrenheit to Celsius
farh = int(input("Enter farheniet: "))

def farh_to_cel(farh):
    cel = float(((farh -32) * 5)/9)
    return cel

print("{:.2f}".format(farh_to_cel(farh)))
