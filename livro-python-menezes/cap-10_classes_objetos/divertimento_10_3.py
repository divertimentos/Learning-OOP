""" Modifique a classe televisão de forma que, se pedirmos para mudar o canal para baixo para além do mínimo,

ela volta para o canal máximo.

Se mudarmos para cima para além do canal máximo,
que volte ao canal mínimo."""

class Televisao:
    def __init__(self, minimo=2, maximo=14):
        self.ligada = False
        self.canal = 2
        self.cmin = minimo
        self.cmax = maximo

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin

tv = Televisao(2, 10)
print(f"Canal inicial: {tv.canal}")

tv.muda_canal_para_baixo()
print(f"Canal novo: {tv.canal}")
