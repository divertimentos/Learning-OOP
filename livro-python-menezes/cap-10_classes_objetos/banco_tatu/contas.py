class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = list()
        self.deposito(saldo, show_message=False)

    def resumo(self):
        print(f"\nConta-corrente nº: {self.numero}")
        print(f"Saldo: R$ {self.saldo:.2f}")
        
        for cliente in self.clientes:
            print(f"\nNome: {cliente.nome}\nTelefone: {cliente.telefone}\n")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['Saque', valor])
            print(f"Saque de R$ {valor}: êxito.")
        else:
            print(f"Seu saque é de R$ {self.saldo}. Não foi possível completar a operação.")
    
    def deposito(self, valor, show_message=True):
        self.saldo += valor
        self.operacoes.append(['DEPOSITO', valor])
        if show_message:
            print(f"Depósito de R$ {valor} feito com êxito!")

    def extrato(self):
        print(f"\nExtrato CC nº: {self.numero}")
        for operacao in self.operacoes:
            print(f"{operacao[0], operacao[1]}")
        print(f"\n Saldo: {self.saldo:2.2f}")