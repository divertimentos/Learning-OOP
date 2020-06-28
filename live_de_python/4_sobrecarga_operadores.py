class Dois:
    val = 2
    def __neg__(self):
        print("Olha só: negativei!")

    def __pos__(self):
        print("Olha só: positivei!")

class MinhaString:
    def __init__(self):
        self.s = "Live de Python"

    def __neg__(self):
        return self.s[::-1]


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self):
        return Ponto(-self.x, -self.y)

    def __pos__(self):
        return Ponto(+self.x, +self.y)

    def __repr__(self):
        return f"Ponto({self.x}, {self.y})"
