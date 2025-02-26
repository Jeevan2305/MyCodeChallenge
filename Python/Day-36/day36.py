# Handle exceptions for division by zero.
def div_by_zero(n, d):
    try:
        result = n/d
        return result
    except ZeroDivisionError:
        print("Division by zero")
        return None

numerator = int(input("Enter Numerator = "))
denominator = int(input("Enter Denominator = "))

print(div_by_zero(numerator, denominator))
