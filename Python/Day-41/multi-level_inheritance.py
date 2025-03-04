# Multi-level Inheritance
class Grandmother:
    generation = 1
    gender = 'F'
    isAdult = True
class Father(Grandmother):
    generation = 2
    gender = 'M'
    
class Son(Father):
    generation = 3
    isAdult = False
    
grandmother = Grandmother()
father = Father()
son = Son()

print(grandmother.generation)
print(grandmother.gender)
print(grandmother.isAdult)

print(father.generation)
print(father.gender)
print(father.isAdult)

print(son.generation)
print(son.gender)
print(son.isAdult)
