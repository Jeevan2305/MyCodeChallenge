num = int(input("Enter a number : "))

def fact_of_number(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "Factorial is not defined for negative numbers"
    else:
        return n * fact_of_number(n - 1)

fact_of_number(num)
