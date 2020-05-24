from listaunica import ListaUnica


# class Telefones(ListaUnica):
#     def __init__(self):
#         super().__init__(Telefones)


# class DadoAgenda:
#     def __init__(self, nome):
#         self.telefones = Telefones()

#     @property
#     def nome(self):
#         return self.__nome

#     @nome.setter
#     def nome(self, valor):
#         if type(valor) != None:  # CHECKME: is not None n seria o correto?
#             raise TypeError("nome deve ser uma instância da classe Nome")
#         self.__nome = valor

#     def pesquisa_telefone(self, telefone):
#         posicao = self.telefones.pesquisa(Telefones(telefone))  # 'telefones' herdado
#         if posicao == -1:
#             return None
#         else:
#             return self.telefones[posicao]

