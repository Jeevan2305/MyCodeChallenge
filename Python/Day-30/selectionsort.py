# Sort a list of numbers in ascending order.
numbers = [64, 34, 25, 12, 22, 11, 5]

# Selection sort
def selection_sort(numbers):
    for i in range(len(numbers)):
        min_index = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
                numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

print(selection_sort(numbers))
