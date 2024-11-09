conta1 = 1000
conta2 = 1500
conta3 = 2000
conta4 = 1340


def verificar_saldo(conta):
    return conta


def adicionar_valor(conta, valor):
    conta += valor
    return conta


def subtrair_valor(conta, valor):
    conta -= valor
    return conta


while True:
    conta = input("Olá, digite sua conta (ou 'sair' para encerrar): ")

    if conta == "sair":
        break  # Sai do loop e encerra o programa

    if conta == "conta1":
        operacao = input(
            "Escolha a operação: \n1 - Saldo\n2 - Adicionar\n3 - Subtrair\n"
        )
        if operacao == "1":
            print("Saldo da Conta 1: R$ ", verificar_saldo(conta1))
        elif operacao == "2":
            valor = float(input("Digite o valor a ser adicionado: "))
            conta1 = adicionar_valor(conta1, valor)
            print("Saldo da Conta 1: R$ ", verificar_saldo(conta1))
        elif operacao == "3":
            valor = float(input("Digite o valor a ser subtraído: "))
            conta1 = subtrair_valor(conta1, valor)
            print("Saldo da Conta 1: R$ ", verificar_saldo(conta1))
        else:
            print("Operação inválida.")

    elif conta == "conta2":
        operacao = input(
            "Escolha a operação: \n1 - Saldo\n2 - Adicionar\n3 - Subtrair\n"
        )
        if operacao == "1":
            print("Saldo da Conta 2: R$ ", verificar_saldo(conta2))
        elif operacao == "2":
            valor = float(input("Digite o valor a ser adicionado: "))
            conta2 = adicionar_valor(conta2, valor)
            print("Saldo da Conta 2: R$ ", verificar_saldo(conta2))
        elif operacao == "3":
            valor = float(input("Digite o valor a ser subtraído: "))
            conta2 = subtrair_valor(conta2, valor)
            print("Saldo da Conta 2: R$ ", verificar_saldo(conta2))
        else:
            print("Operação inválida.")

    elif conta == "conta3":
        operacao = input(
            "Escolha a operação: \n1 - Saldo\n2 - Adicionar\n3 - Subtrair\n"
        )
        if operacao == "1":
            print("Saldo da Conta 3: R$ ", verificar_saldo(conta3))
        elif operacao == "2":
            valor = float(input("Digite o valor a ser adicionado: "))
            conta3 = adicionar_valor(conta3, valor)
            print("Saldo da Conta 3: R$ ", verificar_saldo(conta3))
        elif operacao == "3":
            valor = float(input("Digite o valor a ser subtraído: "))
            conta3 = subtrair_valor(conta3, valor)
            print("Saldo da Conta 3: R$ ", verificar_saldo(conta3))
        else:
            print("Operação inválida.")

    elif conta == "conta4":
        operacao = input(
            "Escolha a operação: \n1 - Saldo\n2 - Adicionar\n3 - Subtrair\n"
        )
        if operacao == "1":
            print("Saldo da Conta 4: R$ ", verificar_saldo(conta4))
        elif operacao == "2":
            valor = float(input("Digite o valor a ser adicionado: "))
            conta4 = adicionar_valor(conta4, valor)
            print("Saldo da Conta 4: R$ ", verificar_saldo(conta4))
        elif operacao == "3":
            valor = float(input("Digite o valor a ser subtraído: "))
            conta4 = subtrair_valor(conta4, valor)
            print("Saldo da Conta 4: R$ ", verificar_saldo(conta4))
        else:
            print("Operação inválida.")

    else:
        print("Conta não encontrada.")
