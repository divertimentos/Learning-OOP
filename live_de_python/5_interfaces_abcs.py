""" 'Embora Python seja uma linguagem dinamicamente tipada, 
é uma linguagem fortemente tipada.
# Quando eu falo que a é uma lista, 
# a é uma lista e sempre vai ser uma lista 
# enquanto ela existir na memória.' """

# duck-typing: listas não são containers mas se comportam como.

from typing import Container


print(isinstance(list, Container))  # False

# print(isinstance(type(list)), Container)  # False

print(isinstance(type([1, 2, 3, 4, 5]), Container))  # False

lista = [1, 2, 3, 4, 5]

print(1 in lista)  # True

print(issubclass(type(lista), Container))

# class Time:
#     def __init__(self, *membros):
#         self.__membros = list()
#         self.__membros.append(membros)
# 
#     def __repr__(self):
#         return self.membros
# 
#     def __len__(self):
#         return len(self.__membros)
# 
#     def __contains__(self, member):
#         return member in self.__membros

""""Exemplo 1: implementando um Container"""

# from collections.abc import Container, Sized
# 
# 
# class Caixa(Container, Sized):
#     def __init__(self, seq):
#         self.seq = seq
# 
#     def __contains__(self, outro):
#         return outro in self.seq
# 
#     def __len__(self):
#         return len(self.seq)
# 
#     def __iter__(self):
#         return self

"""Exemplo 2:

Se conta como uma sequência e tem itens como uma sequência,

então é uma sequência!"""

# from collections.abc import Sequence
# 
# class MinhaTupla(Sequence):
#     def __init__(self, *vals):
#         self.vals = vals
# 
#     def __getitem__(self, pos):
#         return self.vals[pos]
# 
#     def __len__(self):
#         return self.vals[pos]

from collections.abc import MutableSequence

class MinhaLista(MutableSequence):
    def __init__(self, *vals):
        self.vals = vals

    def __getitem__(self, pos):
        return self.vals[pos]

    def __len__(self):
        return self.vals[pos]

    def __delitem__(self, item):
        del self.vals[item]

    def __setitem__(self, pos, valor):
        self.vals[pos] = valor

    def __insert__(self):
        pass 
