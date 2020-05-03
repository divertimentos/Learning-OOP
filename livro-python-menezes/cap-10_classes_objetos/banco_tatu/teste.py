from contas import Cliente, Conta, ContaEspecial

# joao = Conta('João', '3333-333')
# maria = Conta('Maria', "3333-334")

# joao.resumo()
# joao.saque(1000)
# joao.deposito(1500)
# joao.saque(500)
# joao.deposito(200)
# joao.resumo()
# joao.extrato()

joao = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")

conta1 = Conta([joao], 1, 1000)
conta2 = ContaEspecial([maria, joao], 2, 500, 1000)
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato() 
