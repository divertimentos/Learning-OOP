class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.clientes = clientes
        self.numero = numero
        self.saldo = 0
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
            return True
        else:
            print(f"Seu saque é de R$ {self.saldo}. Não foi possível completar a operação.")
            return False
    
    def deposito(self, valor, show_message=True):
        self.saldo += valor
        self.operacoes.append(['DEPOSITO', valor])
        if show_message:
            print(f"Depósito de R$ {valor} feito com êxito!")

    def extrato(self):
        print("~" * 18)
        print(f"Classe: {self.__class__.__name__}")

        print(f"Extrato CC nº: {self.numero}")
        for operacao in self.operacoes:
            print(f"{operacao[0]} de R$ {operacao[1]}")
        print(f"\nSaldo: R${self.saldo:2.2f}")
        print("~" * 18)


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite
    
    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return True
        else:
            print(f"Seu saque é de R$ {self.saldo}. Não foi possível completar a operação.")
            return False

    def extrato(self):
        print("~" * 18)
        print(f"Classe: {self.__class__.__name__}")
        print(f"Extrato CC nº: {self.numero}")
        for operacao in self.operacoes:
            print(f"{operacao[0]} de R$ {operacao[1]}")
        
        print(f"\nSaldo: R${self.saldo:2.2f}")
        print(f"Limite atual: R$ {self.limite}")
        print("~" * 18)
    
    
