# Operadores unários

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


# Operadores infixos

class Numero:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('__add__')
        return self.val + other

    def __radd__(self, other):
        print('__radd__')
        return self.val + other

# Lista bem loka

class ListaBemLoka(list):
    def __add__(self, val):
        """Soma todos os itens da lista com val"""
        return ListaBemLoka([x + val for x in self])

    def __lshift__(self, val):
        """Fazer append na lista usando <<"""
        self.append(val)
        
    def __rshift__(self, pos):
        """Remove um item com >>"""
        return self.pop(pos)

    def __neg__(self):
        return ListaBemLoka(reversed(self))
    
    def __iadd__(self, val):
        """Toma toos os itens da lista com val e manter no objeto"""
        self = ListaBemLoka([x + val for x in self])
