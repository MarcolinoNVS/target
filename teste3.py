import math


# Classe base para formas geométricas
class FormaGeometrica:
    def calcular_area(self):
        pass


# Classe para representar um círculo
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio**2


# Classe para representar um retângulo
class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura


# Função para calcular a área de uma forma genérica
def calcular_area_forma(forma):
    return forma.calcular_area()


raio = float(input("Digite um numero do circulo e de enter \n"))
largura, altura = map(float, input("Digite dois numero com espaço:\n").split())

# Criar instâncias das formas geométricas
circulo = Circulo(raio)
retangulo = Retangulo(largura, altura)

# Calcular e exibir áreas
print("Área do círculo:", calcular_area_forma(circulo))
print("Área do retângulo:", calcular_area_forma(retangulo))
