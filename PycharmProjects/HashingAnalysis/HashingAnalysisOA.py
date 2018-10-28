import random
import math

class HashTableOA(object):
    hashTable = [-1] * 100
    collisions = 0
    numElements = 0

    def __init__(self, size):
        self.hashTable = [-1] * size
        self.collisions = 0
        self.numElements = 0

    def insertkey(self, index, value):
        # if index is filled then iterate from beginning of list until open index
        if self.hashTable[index] != -1:
            start = 0
            self.collisions += 1
            while self.hashTable[start] != -1:
                start += 1
            self.hashTable[start] = value
        else:
            self.hashTable[index] = value
        self.numElements += 1

    def computehashmod(self, num):
        return num % len(self.hashTable)


class HashTableSC(object):
    hashTable = [[]]
    collisions = 0
    numElements = 0

    def __init__(self, size):
        self.hashTable = [[-1] for i in range(size)]
        self.collisions = 0
        self.numElements = 0

    def insertkey(self, index, value):
        # if value is filled then append bucket to list
        if self.hashTable[index][0] != -1:
            self.collisions += 1
            self.hashTable[index].append(value)
        else:
            self.hashTable[index][0] = value
        self.numElements += 1

    def computehashmod(self, num):
        return num % len(self.hashTable)


def computehashmsq(num, length):
    num *= num

    # not able to perform operations if the squared value is 0
    if num < 1:
        return num

    # getting the base 2 power of the squared number and the length
    numPower = math.log(num, 2)
    lengthPower = math.log(length, 2)

    # subtracting power of the length so that when divided it
    # will remove half of unneeded indices
    numPower -= lengthPower

    # dividing the squared num to remove right most indices
    # and then mod length to remove unneeded left indices
    div = pow(2, math.ceil(numPower/2))
    num = math.floor(num / div)
    num = num % length
    return num


hashOAModOne = HashTableOA(100)
hashOAModTwo = HashTableOA(250)
hashOAModThree = HashTableOA(500)
hashOAMsqOne = HashTableOA(100)
hashOAMsqTwo = HashTableOA(250)
hashOAMsqThree = HashTableOA(500)

hashSCModOne = HashTableSC(100)
hashSCModTwo = HashTableSC(250)
hashSCModThree = HashTableSC(500)
hashSCMsqOne = HashTableSC(100)
hashSCMsqTwo = HashTableSC(250)
hashSCMsqThree = HashTableSC(500)


value = 12345

for i in range(100):
    randNumOne = random.randint(0, 300)

    # computing keys
    keyOneMod = hashOAModOne.computehashmod(randNumOne)
    keyOneMsq = computehashmsq(randNumOne, 100)

    # inserting mod key and mid square key
    hashOAModOne.insertkey(keyOneMod, value)
    hashSCModOne.insertkey(keyOneMod, value)
    hashOAMsqOne.insertkey(keyOneMsq, value)
    hashSCMsqOne.insertkey(keyOneMsq, value)

    if hashOAModOne.numElements % 10 == 0:
        print("load factor OA Mod 1: ", hashOAModOne.numElements / 100, ", # of collisions: ", hashOAModOne.collisions)
        print("load factor SC Mod 1: ", hashSCModOne.numElements / 100, ", # of collisions: ", hashSCModOne.collisions)
        print("load factor OA Msq 1: ", hashOAMsqOne.numElements / 100, ", # of collisions: ", hashOAMsqOne.collisions)
        print("load factor SC Msq 1: ", hashSCMsqOne.numElements / 100, ", # of collisions: ", hashSCMsqOne.collisions)
        print("\n")

print("\n")

for i in range(250):
    randNumTwo = random.randint(0, 750)

    # computing keys
    keyTwoMod = hashOAModTwo.computehashmod(randNumTwo)
    keyTwoMsq = computehashmsq(randNumTwo, 250)

    # inserting keys
    hashOAModTwo.insertkey(keyTwoMod, value)
    hashSCModTwo.insertkey(keyTwoMod, value)
    hashOAMsqTwo.insertkey(keyTwoMsq, value)
    hashSCMsqTwo.insertkey(keyTwoMsq, value)


    if hashOAModTwo.numElements % 25 == 0:
        print("load factor OA Mod 2: ", hashOAModTwo.numElements / 250, ", # of collisions: ", hashOAModTwo.collisions)
        print("load factor SC Mod 2: ", hashSCModTwo.numElements / 250, ", # of collisions: ", hashSCModTwo.collisions)
        print("load factor OA Msq 2: ", hashOAMsqTwo.numElements / 250, ", # of collisions: ", hashOAMsqTwo.collisions)
        print("load factor SC Msq 2: ", hashSCMsqTwo.numElements / 250, ", # of collisions: ", hashSCMsqTwo.collisions)
        print("\n")

print("\n")

for i in range(500):
    randNumThree = random.randint(0, 1500)

    # computing keys
    keyThreeMod = hashOAModThree.computehashmod(randNumThree)
    keyThreeMsq = computehashmsq(randNumThree, 500)

    # inserting keys
    hashOAModThree.insertkey(keyThreeMod, value)
    hashSCModThree.insertkey(keyThreeMod, value)
    hashOAMsqThree.insertkey(keyThreeMsq, value)
    hashSCMsqThree.insertkey(keyThreeMsq, value)

    if hashOAModThree.numElements % 50 == 0:
        print("load factor OA Mod 3: ", hashOAModThree.numElements / 500, ", # of collisions: ", hashOAModThree.collisions)
        print("load factor SC Mod 3: ", hashSCModThree.numElements / 500, ", # of collisions: ", hashSCModThree.collisions)
        print("load factor OA Msq 3: ", hashOAMsqThree.numElements / 500, ", # of collisions: ", hashOAMsqThree.collisions)
        print("load factor SC Msq 3: ", hashSCMsqThree.numElements / 500, ", # of collisions: ", hashSCMsqThree.collisions)
        print("\n")


