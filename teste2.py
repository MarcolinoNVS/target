# Função que verifica se um número é par
def is_even(number):
    return number % 2 == 0


# Função que calcula o fatorial de um número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Função que inverte uma string
def reverse_string(input_string):
    return input_string[::-1]


# Função que verifica se uma lista contém números pares
def contains_even_numbers(numbers):
    for num in numbers:
        if is_even(num):
            return True
    return False


# Exemplo de uso das funções
num = 5
print(f"O fatorial de {num} é {factorial(num)}")

string = "marcos!"
print(f"A string invertida é: {reverse_string(string)}")

numbers = [1, 3, 5, 8, 9]
if contains_even_numbers(numbers):
    print("A lista contém números pares.")
else:
    print("A lista não contém números pares.")
