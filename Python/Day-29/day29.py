# Create a dictionary of words and their frequencies.
def dict_of_words(words):
    word_dict = {}
    for word in words:
        word_dict[word] = len(word)
    return word_dict

words = []
s = int(input("Enter the size of list : "))
for i in range(s):
    words.append(input(f"Enter the word {i+1}: "))

print(dict_of_words(words))
