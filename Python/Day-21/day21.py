# Write a function to reverse a list.
def reverse_list(l):
    b = []
    for i in range(len(l)):
        b.append(l[-(i+1)])
    return b

list = []
n = int(input('Number of elements in the list : '))

for i in range(n):
    ele = int(input(f'Element {i + 1} : '))
    list.append(ele)

print('Original list : ', list)
print('Reversed list : ', reverse_list(list))
