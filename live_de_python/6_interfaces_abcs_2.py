from abc import ABC, abstractmethod
from collections import namedtuple
# Protocolos (revisão)
# Criando meu protocolo
# Filas ou quase isso

# "Interfaces são métodos ou atritutos públicos que outros objetos possam usar
# para se comunicar com outros objetos" - Dusty Phillips

# O subconjunto de métodos públicos de um objeto que lhe permitem
# desempenhar um papel específico em um sistema

# Um método que sempre recebe overridiing, recebe o decorator @abstractmethod


# class MinhaABC(ABC):
# 
#     @abstractmethod
#     def meu_metodo_de_exemplo(self):
#         pass
# 
# 
#     @classmethod
#     @abstractmethod
#     def meu_metodo_de_classe(cls):  # é cls mesmo, né? Tipo, obrigatoriamente
#         pass
# 
# 
#     @staticmethod
#     @abstractmethod
#     def meu_metodo_estatico(self):
#         pass

class Fila(ABC):
    @abstractmethod
    def __init__(self, iteravel):
        self.it = list()

    @abstractmethod
    def entrar(self, obj):
        pass

    @abstractmethod
    def sair(self, pos):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __contains__(self, obj):
        pass

    def __repr__(self):
        pass

# Se nós não implementamos uma classe de fato abstrata,
# sua filha vai herdar diretamente de object
# Basta dar um dir(Supermercado) para conferir

# MRO = Method Resolution Order

class Batatinha:
    def entrar(self):
        print("Batatinha - Entrar")

class Padaria(Fila):
    def __init__(self,):
        self.it = list()

    def entrar(self, obj):
       self.it.append(obj)

    def sair(self, pos):
        return self.it.pop(pos=0)

    def __len__(self):
        return len(self.it)

    def __contains__(self, obj):
        return obj in self.it

    def __repr__(self):
        return f"Fila({self.it})"

pessoa = namedtuple('Pessoa', 'nome idade gestante deficiente')

class Supermercado(Fila):
    def __init__(self,):
        self.it = list()
        self.pri = list()

    def entrar(self, obj):
        if isinstance(obj, pessoa):
            if obj.gestante or obj.deficiente or obj.idade > 64:
                self.pri.append(obj)
            else:
                self.it.append(obj)

        else:
            raise NotImplementedError

    def sair(self, pos=0):
        if self.pri:
            return self.pri.pop(pos)
        else:
            return self.it.pop(pos=0)

    def __len__(self):
        return len(self.it) + len(self.pri)

    def __contains__(self):
        return obj in self.it or obj in self.pri

    def __repr__(self):
        return f"Fila({self.pri + self.it})"

@Fila.register
class Banheiro:
    pass

