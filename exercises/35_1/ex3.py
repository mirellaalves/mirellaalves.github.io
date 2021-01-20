# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1,
# imprima na tela um quadrado feito de asteriscos de lado de tamanho n.
# Por exemplo:
# n = 5

# *****
# *****
# *****
# *****
# *****

# Dica: A função print aceita um parâmetro nomeado end que pode ser utilizado
# para imprimir sem a quebra de linha.
# Por exemplo, print(4, end="") e print(2) irá imprimir 42 e
# depois quebrar a linha.


def draw_square(n):
    for row in range(1, n + 1):
        for column in range(1, n + 1):
            print("*", end="")
        print()


print(draw_square(5))
