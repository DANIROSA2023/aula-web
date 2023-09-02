class ContaCorrente:

    def __init__(self,numero_conta, nome_correntista,saldo=0):
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        return self.nome

    def deposito(self,valor_deposito):
        self.saldo += valor_deposito
        return self.saldo

    def saque(self,valor_saque):
        self.saldo -= valor_saque
        return self.saldo

CC1 = ContaCorrente(250,"Danielle")

print (CC1.__dict__)

CC1.deposito(1000)
print (CC1.__dict__)

CC1.saque(50)
print (CC1.__dict__)