#Single Inheritance
class Father:
    gender = 'M'
    isAdult = True

class Son(Father):
    isAdult = False

father = Father()
son = Son()

print(father.gender)
print(father.isAdult)
print(son.gender)
print(son.isAdult)
