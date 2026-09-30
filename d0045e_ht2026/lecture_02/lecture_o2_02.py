class Square:
    sides = 4

    def __init__(self, l):
        self.length = l


    def area(self):
        return self.length*self.length


    def perimeter(self):
        return 4 * self.length


sq1 = Square(2)
sq2 = Square(4)

print(sq1.area())
print(sq2.perimeter())

print(sq1.sides)
