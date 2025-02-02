n1 = int(input("Enter a number 1 : "))
n2 = int(input("Enter a number 2 : "))
n3 = int(input("Enter a number 3 : "))

if n1 >= n2:
    if n1 >= n3:
        print(f"{n1} is largest")
    else:
        print(f"{n3} is largest")
else:
    if n2 >= n3:
        print(f"{n2} is largest")
    else:
        print(f"{n3} is largest")
