# Write a program that checks if a given input year is a leap year or not
def check_leap_year(year):
    if year % 4 != 0:
        print(f"{y} is not a leap year")
    else:
        if year % 100 == 0 and year % 400 != 0:
            print(f"{y} is not a leap year")
        else:
            print(f"{y} is a leap year")

y = int(input("Enter a year : "))
check_leap_year(y)
