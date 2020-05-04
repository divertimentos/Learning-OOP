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
        def checa_saque(valor):
            if self.saldo >= valor:
                return True
            else:
                return False

        if checa_saque(valor):
            self.saldo -= valor
            self.operacoes.append(['Saque', valor])
            print(f"Saque de R$ {valor}: êxito.")
        else:
            print(f"Seu saldo é de R$ {self.saldo}. Não foi possível sacar R$ {valor}.")
    
    
    
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
        Conta.saque(self, valor)

    def extrato(self):
        Conta.extrato(self)                
        print(f"Limite atual: R$ {self.limite}")
        print(f"\nSaldo disponível: R${self.limite + self.saldo:2.2f}")
    
    
