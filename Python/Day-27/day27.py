# Find the longest word in a sentence.
def find_longest_word(sentence):
    max_word = sentence.split()[0]
    max_length = len(max_word)
    for word in sentence.split():
        if len(word) > max_length:
            max_length = len(word)
            max_word = word
    return max_word

sen = input("Enter sentence : ")
print("Longest word : "+find_longest_word(sen))
