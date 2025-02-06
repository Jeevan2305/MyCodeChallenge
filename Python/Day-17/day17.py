def is_palindrome(s):
    beg = 0
    end = len(s) - 1
    c = 0

    while beg <= end:
        if s[beg] != s[end]:
            c = 1
            break
        beg = beg + 1
        end = end - 1

    if c == 1:
        return "{} is not a palindrome".format(s)
    else:
        return "{} is a palindrome".format(s)

while True:
    user_input = input("Enter the string: ")
    if user_input.isalpha():
        print(is_palindrome(user_input))
    else:
        print("Enter a valid string")
