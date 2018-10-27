import random
class HashTableOA(object):
    hashTable = [-1] * 100
    collisions = 0
    numElements = 0

    def __init__(self, size):
        self.hashTable = [-1] * size
        self.collisions = 0
        self.numElements = 0

    def insertkey(self, index, value):
        if self.hashTable[index] != -1:
            start = 0
            self.collisions += 1
            while self.hashTable[start] != -1:
                start += 1
                self.collisions += 1
            self.hashTable[start] = value
        else:
            self.hashTable[index] = value
        self.numElements += 1

    def computehashmod(self, num):
        return num % len(self.hashTable)


class HashTableSC(object):
    hashTable = [[-1] * 100 for i in range(100)]
    collisions = 0
    numElements = 0

    def __init__(self, size):
        self.hashTable = [[-1] * size for i in range(size)]
        self.collisions = 0
        self.numElements = 0

    def insertkey(self, index, value):
        if self.hashTable[index][0] != -1:
            self.collisions += 1
            start = 0
            while self.hashTable[index][start] != -1:
                start += 1
                self.collisions += 1
            self.hashTable[start] = value
        else:
            self.hashTable[index] = value
        self.numElements += 1

    def computehashmod(self, num):
        return num % len(self.hashTable)


def computehashmsq(self, num):
    num *= num


hashOAModOne = HashTableOA(100)
hashOAModTwo = HashTableOA(250)
hashOAModThree = HashTableOA(500)

hashSCModOne = HashTableSC(100)
hashSCModTwo = HashTableSC(250)
hashSCModThree = HashTableSC(500)

value = 12345

for i in range(100):
    randNumOne = random.randint(0, 300)
    keyOne = hashOAModOne.computehashmod(randNumOne)
    hashOAModOne.insertkey(keyOne, value)
    hashSCModOne.insertkey(keyOne, value)
    if hashOAModOne.numElements % 10 == 0:
        print("load factor OA 1: ", hashOAModOne.numElements / 100, ", # of collisions: ", hashOAModOne.collisions)
        print("load factor SC 1: ", hashSCModOne.numElements / 100, ", # of collisions: ", hashSCModOne.collisions)

print("\n")

for i in range(250):
    randNumTwo = random.randint(0, 750)
    keyTwo = hashOAModTwo.computehashmod(randNumTwo)
    hashOAModTwo.insertkey(keyTwo, value)
    hashSCModTwo.insertkey(keyTwo, value)
    if hashOAModTwo.numElements % 25 == 0:
        print("load factor OA 2: ", hashOAModTwo.numElements / 250, ", # of collisions: ", hashOAModTwo.collisions)
        print("load factor SC 2: ", hashSCModTwo.numElements / 250, ", # of collisions: ", hashSCModTwo.collisions)

print("\n")

for i in range(500):
    randNumThree = random.randint(0, 1500)
    keyThree = hashOAModThree.computehashmod(randNumThree)
    hashOAModThree.insertkey(keyThree, value)
    hashSCModThree.insertkey(keyThree, value)
    if hashOAModThree.numElements % 50 == 0:
        print("load factor OA 3: ", hashOAModThree.numElements / 500, ", # of collisions: ", hashOAModThree.collisions)
        print("load factor SC 3: ", hashSCModThree.numElements / 500, ", # of collisions: ", hashSCModThree.collisions)



