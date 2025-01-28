name = input("Enter your name : ")
age = int(input("Enter your age : "))
height = float(input("Enter your height : "))

#print("Hello I'm %s, My age is %d, My height is %.3f" % (name, age, height))
output = "Hello I'm {}, My age is {}, My height is {a:3.2f}"
print(output.format(name, age, a = height))
