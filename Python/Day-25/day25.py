# Write a function to count the frequency of words in a sentence.
def frequency_of_words(s):
    l = s.split()
    d = {}
    for word in l:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d  

sent = input("Enter Sentence : ")

print(frequency_of_words(sent))
