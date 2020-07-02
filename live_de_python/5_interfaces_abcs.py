""" 'Embora Python seja uma linguagem dinamicamente tipada, 
é uma linguagem fortemente tipada.
# Quando eu falo que a é uma lista, 
# a é uma lista e sempre vai ser uma lista 
# enquanto ela existir na memória.' """

# duck-typing: listas não são containers mas se comportam como.

from typing import Container


print(isinstance(list, Container))  # False

print(isinstance(type(list)), Container)  # False

print(isinstance(type([1, 2, 3, 4, 5]), Container))  # False

lista = [1, 2, 3, 4, 5]

print(1 in lista)  # True

print(issubclass(type(lista), Container))