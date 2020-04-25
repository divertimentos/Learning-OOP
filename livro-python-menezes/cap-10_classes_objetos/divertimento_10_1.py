"""Adicione os atributos tamanho e marca à classe Televisao.
Crie dois objetos Televisao e atribua tamanhos e marcas diferentes.
Depois, imprima o valor desses atributos de forma a confirmar a independência
dos valores de cada instância (objeto)"""

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 50
        self.marca = "Samsung"

tv_normal = Televisao()
print(f"TV está ligada? --> {tv_normal.ligada}")
print(f"Canal da TV: {tv_normal.canal}")
print(f"Tamanho da TV: {tv_normal.tamanho} polegadas")
print(f"Marca da TV: {tv_normal.marca}")