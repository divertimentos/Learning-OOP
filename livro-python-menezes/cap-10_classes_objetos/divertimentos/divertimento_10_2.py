"""Atualmente, a classe Televisao inicializa o canal com 2.
Modifique a classe Televisao de forma a receber o canal inicial em seu construtor"""

class Televisao:
    def __init__(self, minimo, maximo, canal=2):
        self.ligada = False
        self.canal = canal
        self.cmin = minimo
        self.cmax = maximo

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1

tv = Televisao(1, 99, 69)
print(f"Canal inicial: {tv.canal}")