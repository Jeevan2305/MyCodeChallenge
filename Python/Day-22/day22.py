# Write a function to remove duplicates from a list.
def remove_duplicates_1(input_list):
    return list(set(input_list))

def remove_duplicates_2(input_list):
    d = {}
    for item in input_list:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    return list(d.keys())

li = []
n = int(input("Enter the size of the list : "))

for i in range(n):
    ele = int(input("Enter element " + str(i+1) + " : "))
    li.append(ele)

print("Orginal list : ", li)
print("List after removing duplicates : ", remove_duplicates_1(li))
print("List after removing duplicates : ", remove_duplicates_2(li))
