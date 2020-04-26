# Adição de métodos para mudar o canal

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
    
    def muda_canal_para_baixo(self):
        self.canal -= 1
    
    def muda_canal_para_cima(self):
        self.canal += 1

tv = Televisao()
print(f"Canal inicial: {tv.canal}")

tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
print(f"Canal novo: {tv.canal}")

tv.muda_canal_para_baixo()
print(f"Canal mais novo: {tv.canal}")