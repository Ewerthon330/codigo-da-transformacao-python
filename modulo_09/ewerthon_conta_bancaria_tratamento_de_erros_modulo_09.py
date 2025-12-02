class SaldoInsuficienteError(Exception):
    pass

class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def sacar(self,value):
        if value > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente")
        self.saldo -= value
        print(f"Saque realizado com sucesso! Saldo atual: {self.saldo}")


conta = ContaBancaria(100)


try:
    valor_saque = float(input("Digite o valor para sacar: "))
    conta.sacar(valor_saque)
except SaldoInsuficienteError as e:
    print(e)