# Write a function to find the sum of all elements in a list.
def sum_list(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    return sum

list = []
n = int(input("Size of the list : "))

for i in range(n):
    num = int(input(f"Enter the element {i+1} : "))
    list.append(num)

print(f"Sum of elements in list : {sum_list(list)}")
