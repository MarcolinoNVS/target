import random


class TriviaGame:
    def __init__(self):
        self.perguntas = {
            "Quem é o presidente do Brasil em 2022?": [
                "A. Jair Bolsonaro",
                "B. Luiz Inácio Lula da Silva",
                "C. João Doria",
                "D. Ciro Gomes",
            ],
            "Qual é a capital do Japão?": [
                "A. Pequim",
                "B. Seul",
                "C. Tóquio",
                "D. Bangcoc",
            ],
            "Quantos planetas existem no sistema solar?": [
                "A. 7",
                "B. 8",
                "C. 9",
                "D. 10",
            ],
            "Quem escreveu 'Dom Quixote'?": [
                "A. William Shakespeare",
                "B. Miguel de Cervantes",
                "C. Charles Dickens",
                "D. Jane Austen",
            ],
            "Teste1": [
                "A. tes ",
                "B. te",
                "C. tete",
                "D.  teste",
            ],
            "teste2": [
                "A. qweqw",
                "B. asda",
                "C. asdx",
                "D.  abcd",
            ],
        }
        self.pontuacao = 0

    def apresentar_pergunta(self, pergunta, opcoes):
        print(pergunta)
        random.shuffle(opcoes)  # Embaralhar as opções
        for opcao in opcoes:
            print(opcao)

        resposta = input("Escolha a opção correta (A, B, C, ou D): ").upper()

        if resposta in ["A", "B", "C", "D"]:
            indice_resposta = ord(resposta) - ord("A")
            resposta_correta = self.perguntas[pergunta][0]

            if opcoes[indice_resposta] == resposta_correta:
                print("Resposta correta! Você ganhou 1 ponto.\n")
                self.pontuacao += 1
            else:
                print(
                    f"Resposta incorreta. A resposta correta era: {resposta_correta}\n"
                )
        else:
            print("Opção inválida. Por favor, escolha A, B, C ou D.\n")

    def jogar(self):
        print(
            "Bem-vindo ao Quiz do Marcolino!\nResponda às perguntas para ganhar pontos.\n"
        )

        perguntas_nao_respondidas = list(self.perguntas.keys())
        random.shuffle(perguntas_nao_respondidas)

        for pergunta in perguntas_nao_respondidas:
            self.apresentar_pergunta(pergunta, self.perguntas[pergunta])

        print(f"Fim do jogo! Sua pontuação final é: {self.pontuacao}")


if __name__ == "__main__":
    while True:
        jogo = TriviaGame()
        jogo.jogar()

        jogar_novamente = input(
            "Deseja jogar novamente? (Digite 'sim' para jogar novamente, ou 'sair' para sair): "
        ).lower()

        if jogar_novamente != "sim":
            print("Obrigado por jogar. Até a próxima!")
            break
