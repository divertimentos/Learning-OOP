"""Crie classes para representar estados e cidades.
Cada estado tem um nome, sigla e cidades.
Cada cidade tem nome e população.
Escreva um programa de testes que crie três estados com algumas cidades cada um.
Exiba a população de cada estado como a soma da população de suas cidades"""

class Estados:
    def __init__(self, nome, sigla, cidades):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades
    
    def soma_populacao(self):
        soma_populacao = 0
        for cidade in self.cidades:
            soma_populacao += cidade.populacao
        return soma_populacao


class Cidades:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

# Cidades
guarulhos = Cidades("Guarulhos", 1000000)
barueri = Cidades("Barueri", 200000)
diadema = Cidades("Diadema", 50000)

porto_alegre = Cidades("Porto Alegre", 900000)
tramandai = Cidades("Tramandaí", 150000)
igrejinha = Cidades("Igrejinha", 50000)

mordor = Cidades("Mordor", 150000)
magush = Cidades("Magush", 1500)
winterfell = Cidades("Winterfell", 120000)

# Estados
sao_paulo = Estados("São Paulo", "SP", [guarulhos, barueri, diadema])
rio_grande_do_sul = Estados("Rio Grande do Sul", "RS", [porto_alegre, tramandai, igrejinha])
parana = Estados("Paraná", "PR", [mordor, magush, winterfell])

print(f"Soma da população de São Paulo: {sao_paulo.soma_populacao()} habitantes.")
print(f"Soma da população do Rio Grande do Sul: {rio_grande_do_sul.soma_populacao()} habitantes.")
print(f"Soma da população do Paraná: {parana.soma_populacao()} habitantes.")