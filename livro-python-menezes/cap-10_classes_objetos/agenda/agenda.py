from listaunica import ListaUnica
from .agenda import DadoAgenda
from nome import Nome


class TipoTelefone(ListaUnica):
    def __init__(self):
        super().__init__(TipoTelefone)


class Agenda(ListaUnica):
    def __init__(self):
        super().__init__(DadoAgenda)
        self.tipos_telefone = TipoTelefone()

    def adiciona_tipo(self, tipo):
        self.tipos_telefone.adiciona(TipoTelefone(tipo))

    def pesquisa_nome(self, nome):
        if type(nome) == str:
            nome = Nome(nome)
        for dados in self.lista:
            if dados.nome == nome:
                return dados
        else:
            return None

    def ordena(self):
        super().ordena(lambda dado: str(dado.nome))
