# Sort a list of numbers in ascending order.
numbers = [64, 34, 25, 12, 22, 11, 5]

# Bubble sort
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1] :
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

print(bubble_sort(numbers))
