def saudacao(nome):
    return "Olá, " + nome


def pergunta_1(nome):
    lutador = input(
        nome
        + ", desses 4 lutadores, qual deles é o melhor de todos os tempos? jones,spider,gsp,israel:\n "
    )
    lutador = lutador.lower()
    if lutador == "jones":
        return "Cartel invicto, Jones defendeu 14 vezes seu cinturão. Por muitos, é considerado o melhor de todos os tempos."
    elif lutador == "spider":
        return "Maior campeão peso médio da história com seu estilo de lutar semelhante ao de Muhammad Ali."
    elif lutador == "gsp":
        return "Um dos maiores campeões de todo MMA."
    elif lutador == "israel":
        return (
            "Lutador striker mais habilidoso do UFC e de todos os esportes de combate."
        )
    else:
        return "Desconheço esse lutador " + lutador + "."


def estilo(nome):
    estilo_luta = input(nome + ", qual é o seu estilo de luta favorito? jj ou boxe? ")
    if estilo_luta == "jj":
        return "No MMA, é essencial saber pelo menos o mínimo de " + estilo_luta
    elif estilo_luta == "boxe":
        return (
            "Boxe no MMA é uma arte que faz total diferença, porém apenas um "
            + estilo_luta
            + " bom sem nenhum jogo de defesa de grappling pode ser um problema grande."
        )


nome = input("Digite seu nome: ")
mensagem = saudacao(nome)  # Primeiro exibimos a saudação
print(mensagem)
mensagem1 = pergunta_1(nome)
print(mensagem1)  # Em seguida, exibimos a resposta da pergunta
mensagem2 = estilo(nome)

print(mensagem2)

input("Pressione Enter para encerrar o chat")
