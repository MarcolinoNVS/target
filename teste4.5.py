contas = {
    "id123": 1000,
    "id456": 1500,
    "id789": 2000,
}


def verificar_saldo(conta):
    return contas[conta]


def adicionar_valor(conta, valor):
    contas[conta] += valor


def subtrair_valor(conta, valor):
    contas[conta] -= valor


def menu_conta(conta):
    while True:
        operacao = input(
            f"Escolha a operação para {conta}:\n1 - Saldo\n2 - Adicionar\n3 - Subtrair\n4 - Sair\n"
        )

        if operacao == "1":
            print(f"Saldo da {conta}: R$ {verificar_saldo(conta)}")
        elif operacao == "2":
            valor = float(input("Digite o valor a ser adicionado: "))
            adicionar_valor(conta, valor)
            print(f"Saldo da {conta}: R$ {verificar_saldo(conta)}")
        elif operacao == "3":
            valor = float(input("Digite o valor a ser subtraído: "))
            subtrair_valor(conta, valor)
            print(f"Saldo da {conta}: R$ {verificar_saldo(conta)}")
        elif operacao == "4":
            break
        else:
            print("Operação inválida.")


conta = input("Olá, digite o ID da sua conta: ")

if conta in contas:
    menu_conta(conta)
else:
    print("Conta não encontrada.")
