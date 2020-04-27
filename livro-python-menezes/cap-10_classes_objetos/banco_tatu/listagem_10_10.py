from contas import Cliente, Conta
from bancos import Banco

joao = Cliente("João da Silva", "3241-5599")
maria = Cliente("Maria Silva", "7231-9955")
jose = Cliente("José Vargas", "9721-3040")
conta_JM = Conta([joao, maria], 100)
conta_J = Conta([jose], 10)
tatu = Banco("Tatú")
tatu.abre_conta(conta_JM)
tatu.abre_conta(conta_J)
tatu.lista_contas()