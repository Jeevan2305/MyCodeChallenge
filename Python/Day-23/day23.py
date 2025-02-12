# Write a function to find the intersection of two lists.
def intersection(l1, l2):
    for i in range(len(l2)):
        if l2[i] not in l1:
            l1.append(l2[i])
    return l1

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7, 8]

print(intersection(list1, list2))
