import random


def jogar_adivinhacao():
    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Estou pensando em um número entre 1 e 100.")

    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        tentativa = int(input("Tente adivinhar o número: "))
        tentativas += 1

        if tentativa == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif tentativa < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")


if __name__ == "__main__":
    jogar_adivinhacao()
