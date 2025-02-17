# Reverse words in a sentence.
def reverse_words(sentence):
    rev = ""
    for word in sentence.split():
        rev += word[::-1] + " "
    return rev.strip()

sen = input("Enter sentence : ")
print("Reverse sentence : " + reverse_words(sen))
