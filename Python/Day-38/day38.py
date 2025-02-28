# Create a custom exception class.
class DivisibleByTenError(Exception):
    pass

number = int(input("Enter a number : "))

try:
    if number % 10 != 0:
        print(f"{number} : Not divisible by ten")
    else:
        raise DivisibleByTenError(number)
except DivisibleByTenError as e:
    print(f"Exception occured : {e}")
