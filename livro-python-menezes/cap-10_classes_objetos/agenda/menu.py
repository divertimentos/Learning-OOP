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

