import sys
import pickle
from functools import total_ordering


def nulo_ou_vazio(texto):
    return texto is None or not texto.strip()


def valida_faixa_inteiro(pergunta, inicio, fim, padrao=None):
    while True:
        try:
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada) and padrao is not None:
                entrada = padrao
            valor = int(entrada)
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}.")


def valida_faixa_inteiro_ou_branco(pergunta, inicio, fim):
    while True:
        try:
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada):
                return None
            valor = int(entrada)
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}.")


class ListaUnica:
    def __init__(self, elem_class):
        self.lista = []
        self.elem_class = elem_class

    def __len__(self):
        return len(self.lista)

    def __iter__(self):
        return iter(self.lista)

    def __getitem__(self, p):
        return self.lista[p]

    def indice_valido(self, i):
        return i >= 0 and i < len(self.lista)

    def adiciona(self, elem):
        if self.pesquisa(elem) == -1:
            self.lista.append(elem)

    def remove(self, elem):
        self.lista.remove(elem)

    def pesquisa(self, elem):
        self.verifica_tipo(elem)
        try:
            return self.lista.index(elem)
        except ValueError:
            return -1

    def verifica_tipo(self, elem):
        if not isinstance(elem, self.elem_class):
            raise TypeError("Tipo inválido")

    def ordena(self, chave=None):
        self.lista.sort(key=chave)


@total_ordering  # Implementa todos os operadores de comparação
class Nome:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

    def __repr__(self):
        return f"<Classe {(type(self).__name__)} em 0x{id(self):x} Nome: {self.__nome} Chave: {self.__chave}>"

    def __eq__(self, outro):
        return self.nome == outro.nome

    def __lt__(self, outro):
        return self.nome < outro.nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if nulo_ou_vazio(valor):
            raise ValueError("Nome não pode ser nulo nem em branco")
        self.__nome = valor
        self.__chave = Nome.CriaChave(valor)

    @property
    def chave(self):
        return self.__chave

    @staticmethod  # Cria um método estático
    def CriaChave(nome):
        return nome.strip().lower()


@total_ordering
class TipoTelefone:
    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f"({self.tipo})"

    def __eq__(self, outro):
        if outro is None:
            return False
        return self.tipo == outro.tipo

    def __lt__(self, outro):
        return self.tipo < outro.tipo


class Telefone:
    def __init__(self, numero, tipo=None):
        self.numero = numero
        self.tipo = tipo

    def __str__(self):
        if self.tipo is not None:
            tipo = self.tipo
        else:
            tipo = ""
        return f"{self.numero} {tipo}"

    def __eq__(self, outro):
        return self.numero == outro.numero and (
            (self.tipo == outro.tipo) or (self.tipo is None or outro.tipo is None)
        )

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, valor):
        if nulo_ou_vazio(valor):
            raise ValueError("Número nnao opde ser None ou em branco.")
        self.__numero = valor


class Telefones(ListaUnica):
    def __init__(self):
        super().__init__(Telefone)  # CHECKME: Telefone ou Telefones?


class TiposTelefone(ListaUnica):
    def __init__(self):
        super().__init__(TipoTelefone)


class DadoAgenda:
    def __init__(self, nome):
        self.nome = nome
        self.telefones = Telefones()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, Nome):
            raise TypeError("nome deve ser uma instância da classe Nome")
        self.__nome = valor

    def pesquisa_telefone(self, telefone):
        posicao = self.telefones.pesquisa(Telefone(telefone))
        if posicao == -1:
            return None
        else:
            return self.telefones[posicao]


class Agenda(ListaUnica):
    def __init__(self):
        super().__init__(DadoAgenda)
        self.tipos_telefone = TiposTelefone()

    def adiciona_tipo(self, tipo):
        self.tipos_telefone.adiciona(TipoTelefone(tipo))

    def pesquisa_nome(self, nome):
        if isinstance(nome, str):
            nome = Nome(nome)
        for dados in self.lista:
            if dados.nome == nome:
                return dados
        else:
            return None

    def ordena(self):
        super().ordena(lambda dado: str(dado.nome))


class Menu:
    def __init__(self):
        self.opcoes = [["Sair", None]]

    def adiciona_opcao(self, nome, funcao):
        self.opcoes.append([nome, funcao])

    def exibe(self):
        print("===")
        print("Menu")
        print("===\n")
        for i, opcao in enumerate(self.opcoes):
            print(f"[{i} - {opcao[0]}]")
        print()

    def execute(self):
        while True:
            self.exibe()
            escolha = valida_faixa_inteiro(
                "Escolha uma opção: ", 0, len(self.opcoes) - 1
            )
            if escolha == 0:
                break
        self.opcoes[escolha][1]()


class AppAgenda:
    @staticmethod
    def pede_nome():
        return input("Nome: \n")

    @staticmethod
    def pede_telefone():
        return input("Telefone: \n")

    @staticmethod
    def mostra_dados(dados):
        print(f"Nome: {dados.nome}")
        for telefone in dados.telefones:
            print("Telefone: {telefone}")
        print()

    @staticmethod
    def mostra_dados_telefone(dados):
        print(f"Nome: {dados.nome}")
        for i, telefone in enumerate(dados.telefones):
            print(f"{i} - {telefone}")
        print()

    @staticmethod
    def pede_nome_arquivo():
        return input("Nome do arquivo: \n")

    def __init__(self):
        self.agenda = Agenda()
        self.agenda.adiciona_tipo("Celular")
        self.agenda.adiciona_tipo("Residência")
        self.agenda.adiciona_tipo("Trabalho")
        self.agenda.adiciona_tipo("Fax")
        self.menu = Menu()
        self.menu.adiciona_opcao("Novo", self.novo)
        self.menu.adiciona_opcao("Altera", self.altera)
        self.menu.adiciona_opcao("Apaga", self.apaga)
        self.menu.adiciona_opcao("Lista", self.lista)
        self.menu.adiciona_opcao("Grava", self.grava)
        self.menu.adiciona_opcao("Lê", self.le)
        self.menu.adiciona_opcao("Ordena", self.ordena)

    def pede_tipo_telefone(self, padrao=None):
        for i, tipo in enumerate(self.agenda.tipos_telefone):
            print(f"{i} - {tipo}", end=None)
        t = valida_faixa_inteiro(
            f"Tipo: ", 0, len(self.agenda.tipos_telefone) - 1, padrao
        )
        return self.agenda.tipos_telefone[t]

    def pesquisa(self, nome):
        dado = self.agenda.pesquisa_nome(nome)
        return dado

    def novo(self):
        novo = AppAgenda.pede_nome()
        if nulo_ou_vazio(novo):
            return
        nome = Nome(novo)
        if self.pesquisa(nome) != None:
            print(f"Nome já existe!")
            return
        registro = DadoAgenda(nome)
        self.menu_telefones(registro)
        self.agenda.adiciona(registro)

    def apaga(self):
        if len(self.agenda) == 0:
            print(f"Agenda vazia, nada a apagar")
        nome = AppAgenda.pede_nome()
        if nulo_ou_vazio(nome):
            return
        p = self.pesquisa(nome)
        if p != None:
            self.agenda.remove(p)
            print(f"Apagado. A agenda agora possui apenas: {self.agenda} registros")
        else:
            print(f"Nome não encontrado")

    def altera(self):
        if len(self.agenda) == 0:
            print(f"Agenda vazia, nada a alterar")
        nome = AppAgenda.pede_nome()
        if nulo_ou_vazio(nome):
            return
        p = self.pesquisa(nome)
        if p != None:
            print(f"\nEncontrado:\n")
            AppAgenda.mostra_dados(p)
            print(f"Digite ENTER caso não queira alterar o nome")
            novo = AppAgenda.pede_nome()
            if not nulo_ou_vazio(novo):
                p.nome = Nome(novo)
            self.menu_telefones(p)
        else:
            print(f"Nome não encontrado!")

    def menu_telefones(self, dados):
        while True:
            print(f"\nEditando telefones\n")
            AppAgenda.mostra_dados_telefone(dados)
            if len(dados.telefones) > 0:
                print(f"\n[A] - alterar\n[D] - apagar\n", end="")
            print(f"[N] - novo\n[S] - sair\n")
            operacao = input("Escolha uma operação: \n")
            operacao = operacao.lower()
            if operacao not in ["a", "d", "n", "s"]:
                print("Operação inválida. Digite A, D, N ou S")
                continue
            if operacao == "a" and len(dados.telefones) > 0:
                self.altera_telefones(dados)
            elif operacao == "d" and len(dados.telefones) > 0:
                self.apaga_telefones(dados)
            elif operacao == "n":
                self.novo_telefone(dados)
            elif operacao == "s":
                break

    def novo_telefone(self, dados):
        telefone = AppAgenda.pede_telefone()
        if nulo_ou_vazio(telefone):
            return
        if dados.pesquisa_telefone(telefone) != None:
            print("Telefone já existe")
        tipo = self.pede_tipo_telefone()
        dados.telefones.adiciona(Telefone(telefone, tipo))

    def apaga_telefone(self, dados):
        t = valida_faixa_inteiro_ou_branco(
            "Digite a posição do número a apagar, ENTER para sair:",
            0,
            len(dados.telefones) - 1,
        )
        if t is None:
            return
        dados.telefones.remove(dados.telefones[t])

    def altera_telefones(self, dados):
        t = valida_faixa_inteiro_ou_branco(
            "Digite a posição do número a alterar, ENTER para sair:",
            0,
            len(dados.telefones) - 1,
        )
        if t is None:
            return

        telefone = dados.telefones[t]
        print(f"Telefone: {telefone}")
        print(f"Digite ENTER caso não queira alterar o número")
        novo_telefone = AppAgenda.pede_telefone()
        if not nulo_ou_vazio(novo_telefone):
            telefone.numero = novo_telefone
        print("Digite ENTER caso não queira alterar o tipo")
        telefone.tipo = self.pede_tipo_telefone(
            self.agenda.tipos_telefone.pesquisa(telefone.tipo)
        )

    def lista(self):
        print("\nAgenda")
        print("-" * 60)
        for e in self.agenda:
            AppAgeda.mostra_dados(e)
        print("-" * 60)

    def le(self, nome_arquivo=None):
        if nome_arquivo is None:
            nome_arquivo = AppAgenda.pede_nome_arquivo()
        if nulo_ou_vazio(nome_arquivo):
            return
        with open(nome_arquivo, "rb") as arquivo:
            self.agenda = pickle.load(arquivo)
        self.ultimo_nome = nome_arquivo

    def ordena(self):
        self.agenda.ordena()
        print("\nAgenda ordenada\n")

    def grava(self):
        if self.ultimo_nome != None:
            print(f"Último nome utilizado foi {self.ultimo_nome}")
            print(f"Digite ENTER caso queira utiliza o mesmo nome")
        nome_arquivo = AppAgenda.pede_nome_arquivo()
        if nulo_ou_vazio(nome_arquivo):
            if self.ultimo_nome != None:
                nome_arquivo = self.ultimo_nome
            else:
                return
        with open(nome_arquivo, "wb") as arquivo:
            pickle.dump(self.agenda, arquivo)

    def execute(self):
        self.menu.execute()


if __name__ == "__main__":
    app = AppAgenda()
    if len(sys.argv) > 1:
        app.le(sys.argv[1])
    app.execute()
