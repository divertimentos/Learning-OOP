# 1. Numerador
# 2. Denominador

# Métodos:
# Somar, subtrair, multiplicar, dividir (...)

class Fracao:
    def __init__(self, num, den):
        self.numerador = num
        if den == 0:
            self.denominador = 1
        else:
            self.denominador = den

#    def somar():

    def subtrair(self, outra):
        return self.somar(outra.negar())  # Eita!

#    def inverter(self):

    def multiplicar(self, outra):
        num = self.numerador * outra.numerador
        den = self.denominador * outra.denominador
        return Fracao(num, den)

    def dividir(self, outra):
        return self.multiplicar(outra.inverter())  # EITA!