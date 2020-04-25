# Modelagem de uma televisão

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
tv = Televisao()

print(tv.ligada)
print(f"Canal da TV: {tv.canal}")

tv_sala = Televisao()
tv_sala.ligada = True
tv_sala.canal = 4

# print(f"Canal da TV (Sala): {tv_sala.canal}")