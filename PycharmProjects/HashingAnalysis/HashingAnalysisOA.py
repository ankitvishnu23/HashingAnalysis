import random
class HashTableOA(object):
    hashTable = [""] * 100
    collisions = 0
    numElements = 0

    def __init__(self, size):
        self.hashTable = [-1] * size
        self.collisions = 0
        self.numElements = 0

    def insertkey(self, index, value):
        # if self.filled():
        #     return
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

    # def filled(self):
    #     if floor(self.numElements / len(self.hashTable)) == self.loadFactor:
    #         return True
    #     else:
    #         return False


def computehashmsq(self, num):
    num *= num


hashOAmod = HashTableOA(100)
value = "hello"

for i in hashOAmod.hashTable:
    randNum = random.randint(0, 300)
    key = hashOAmod.computehashmod(randNum)
    hashOAmod.insertkey(key, value)
    if hashOAmod.numElements % 10 == 0:
        print("load factor: ", hashOAmod.numElements / 100, ", # of collisions: ", hashOAmod.collisions)



