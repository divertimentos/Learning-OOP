from contas import Conta

joao = Conta('João', '3333-333')
maria = Conta('Maria', "3333-334")

joao.resumo()
joao.saque(1000)
joao.deposito(1500)
joao.saque(500)
joao.deposito(200)
joao.resumo()
joao.extrato()
