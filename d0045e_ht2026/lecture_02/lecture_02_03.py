class Cube:
    __sides = 6
    __edges = 12

    def __init__(self, l):
        if l < 0:
            l = 1
        self.__length = l

    def getLength(self):
        return self.__length

    def setLength(self, l):
        if l < 0:
            l = 1
        self.__length = l

    def getSides(self):
        return self.__sides

    def getSides2(cls):
        return cls.__sides

    def isValid(length):
        if (length > 0):
            print("Valid edge length")
        else:
            print("Invalid value")



c = Cube(4)

print(c.getLength())
print(c.getSides())

print(Cube.getSides2(Cube))

Cube.isValid(-4)