import random

# 1. Write a program that generates a random number. 
n = random.randint(0, 100)
print(n)

# 2. Write a program that generates random number between 2 integers
start = int(input("Enter Start : "))
end = int(input("Enter End : "))

c = random.randint(start, end)
print(c)
