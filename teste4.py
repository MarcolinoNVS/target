class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def verificar_saldo(self):
        return self.saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}"
        else:
            return "Valor de depósito inválido."

    def retirar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"Retirada de R${valor} realizada com sucesso. Saldo atual: R${self.saldo}"
        else:
            return "Saldo insuficiente ou valor de retirada inválido."


# Criar uma conta bancária
minha_conta = ContaBancaria()

# Verificar o saldo inicial
print(f"Saldo Inicial: R${minha_conta.verificar_saldo()}")

# Realizar um depósito
print(minha_conta.depositar(100))

# Realizar uma retirada
print(minha_conta.retirar(30))

# Verificar o saldo atual
print(f"Saldo Atual: R${minha_conta.verificar_saldo()}")
