# Write a function to calculate the Fibonacci sequence up to a certain limit.
def fibonacci(number):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= number:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

num = int(input('Number of Fibonacci sequences'))
print(fibonacci(num))
