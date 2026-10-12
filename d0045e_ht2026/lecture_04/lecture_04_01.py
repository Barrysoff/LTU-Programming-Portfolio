class Hypercube:

    def __init__(self, n, l):
        self._dimension = n
        self._length = l

    def getDimension(self):
        return self._dimension

    def getLength(self):
        return self._length

    def setLength(self, l):
        if l < 0:
            raise ValueError("Length must be non-negative")
        self._length = l

    def whatAmI(self):
        print("I am a", self._dimension, "dimensional hypercube")


class Square(Hypercube):

    def __init__(self, l):
        super().__init__(2, l)
        self._edges = 4

    def getEdges(self):
        return self._edges

    def area(self):
        return self._length * self._length

    def whatAmI(self):
        print("I am a square")

hc1 = Hypercube(5, 2)
hc1.whatAmI()
print(hc1.getLength())
#hc1.setLength(-9)

sq1 = Square(4)
sq1.whatAmI()
print(sq1.getLength())
print(sq1.area())

class Cube(Hypercube):

    def __init__(self, l):
        super().__init__(3, l)

    def volume(self):
        return self._length * self._length * self._length

    def whatAmI(self):
        print("I am a cube")

cu1 = Cube(3)
print(cu1.volume())
