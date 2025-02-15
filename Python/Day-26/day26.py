# Write a function check if two strings are anagrams.
def are_anagrams_1(str1, str2):
    return sorted(str1) == sorted(str2)

def are_anagrams_2(str1, str2):
    d1 = {}
    d2 = {}
    for char in str1:
        if char in d1:
            d1[char] += 1
        else:
            d1[char] = 1
    for char in str2:
        if char in d2:
            d2[char] += 1
        else:
            d2[char] = 1
    return d1 == d2

s1 = input("Enter a string 1 : ")
s2 = input("Enter a string 2 : ")

print(are_anagrams_1(s1, s2))
print(are_anagrams_2(s1, s2))
