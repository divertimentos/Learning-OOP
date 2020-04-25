# Verificação da faixa de canais de TV

class Televisao:
    def __init__(self, minimo, maximo):
        self.ligada = False
        self.canal = 2
        self.cmin = minimo 
        self.cmax = maximo

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1

tv = Televisao(1, 99)

for x in range(0, 120):
    tv.muda_canal_para_cima()

print(tv.canal)

for x in range(0, 120):
    tv.muda_canal_para_baixo()
print(tv.canal)