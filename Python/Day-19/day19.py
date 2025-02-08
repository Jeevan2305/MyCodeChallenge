# Write a function to find the maximum element in a list.
def max_element(l):
    if len(l) == 0:
        return None
    max_element = l[0]
    for i in range(1, len(l)):
        if l[i] > max_element:
            max_element = l[i]
    return max_element

list = []
n = int(input("Enter the number of elements : "))

for i in range(n):
    element = int(input(f"Enter the element {i+1} : "))
    list.append(element)

print(f"Max element : {max_element(list)}" )
