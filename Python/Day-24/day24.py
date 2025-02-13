# Write a function to convert a list of words into a sentence.
def word_to_list_1(l):
    return ' '.join(l)

def word_to_list_2(l):
    sen = ""
    for word in l:
        sen += word
        sen += ' '
    return sen.strip()

word = []
n = int(input("Enter the no of words to convert : "))
for i in range(n):
    word.append(input(f"Enter the word {i+1}: "))

print(word_to_list_1(word))
print(word_to_list_2(word))
