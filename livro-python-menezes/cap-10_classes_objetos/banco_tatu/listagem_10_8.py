from cliente import Cliente
from contas import Conta

maria = Cliente("Maria da Silva", "555-4321")
joao = Cliente("João da Silva", "777-1234")

# conta = Conta([maria, joao], 1234, 500)
# conta1.saque(50)
# conta2.deposito(300)
# conta1.saque(50)
# conta2.deposito(300)
# conta1.saque(190)
# conta2.deposito(95.15)
# conta2.saque(250)
# conta1.extrato()
# conta2.extrato()
# conta1.saque(750)
# conta.resumo()

jo_jo = Cliente(["João", "José"], "3261-4556")
conta_jojo = Conta(jo_jo, 2222, saldo=500)

conta_jojo.resumo()