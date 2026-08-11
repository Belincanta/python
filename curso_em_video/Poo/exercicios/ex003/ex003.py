#declaração da classe
class ContaBancaria: 
    """
    Cria uma conta bancária e realiza saques e depositos
    """
    def __init__(self, id, nome, saldo = 0): #método constutor
        self.id_conta = id
        self.nome_titular = nome
        self.saldo = saldo
        print("="*60)
        print(f"Conta {self.id_conta} criada com sucesso com saldo de R${self.saldo:.2f}.")
        print("="*60)

    def __str__(self): #função para poder usar o print(c1) direto.
        return f"= A conta {self.id_conta} de {self.nome_titular} tem R${self.saldo:.2f} de saldo bancário."

    def depositar(self, valor):
        self.saldo += valor
        print(f"+ Deposito de R${valor:.2f} autorizado na conta {self.id_conta}.")

    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            print(f"- Saque de R${valor:.2f} autorizado na conta {self.id_conta}.")
        else:
            print(f"x' Saque de R${valor:.2f} não autorizado na conta {self.id_conta}, não possui saldo disponível.")

#declaração do objeto
c1 = ContaBancaria(id=115, nome="Alessandro", saldo=1500)
c1.depositar(500)
c1.sacar(3000)
print(c1)