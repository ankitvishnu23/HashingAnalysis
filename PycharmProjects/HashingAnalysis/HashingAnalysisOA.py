class hashTable:
    hashTable = [0] * 10;
    collisions = 0;
    def computehash(self, x, hashTable):
        return x % len(hashTable)

    def insertkey(self, hashTable, key, value, collisions):
        index = computehash(x, hashTable)
        if hashTable[index] == 0:
            start = 0
            collisions += 1
            while hashTable[start] == 0:
                start += 1
            hashTable[start] = value
        else:
            hashTable[index] == value
        return collisions
