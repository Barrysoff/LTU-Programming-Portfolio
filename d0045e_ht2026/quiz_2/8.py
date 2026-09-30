class Plant:

    def __init__(self, c, t):
        self.color = c
        self.type = t

class Edible:

    def __init__(self, n):
        self.nutrition = n

    def eatMe(self):
        print("You are now less hungry")

class Potato(Edible, Plant):

    def __init__(self, c, t, n):
        Plant.__init__(self, c, t)
        Edible.__init__(self, n)

    def eatMe(self):
        print("You have now eaten a", self.type)

p = Potato("brown", "potato", 100)
p.eatMe()
q = Potato("yellow", "yam", 150)
q.eatMe()