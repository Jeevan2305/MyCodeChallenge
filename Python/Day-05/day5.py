# If-else Statements
# Write a program that takes an integer as input and checks if it's even or odd.
n = int(input("Enter a number : "))
if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")

# Write a program that takes an age as input and determines if the person is a child, teenager, adult, or senior citizen.
age = int(input("Enter a age : "))
if age <= 12:
    print("Child")
elif age > 12 and age <= 18:
    print("Teenager")
elif age > 18 and age <= 65:
    print("Adult")
else:
    print("Senior Citizen")

# Nested If-else Statements
# Using nested if-else, write a program that takes three numbers as input and determines the largest among them.
n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))
n3 = int(input("Enter number 3 : "))

if n1 >= n2:
    if n1 >= n3:
        print(n1)
    else:
        print(n2)
else:
    if n2 >= n3:
        print(n2)
    else:
        print(n3)

# For Loop
# Write a program to calculate the sum of all numbers up to the given input number.
num = int(input("Enter a number num : "))
sum = 0

for i in range(1, num+1):
    sum += i

print(sum)

# While Loop
# Write a program to calculate the factorial of a given number.
n = int(input("Enter a number n : "))
fact = 1

while n >= 0:
    if n == 0 or n == 1:
        break
    fact *= n
    n = n - 1

print(fact)
