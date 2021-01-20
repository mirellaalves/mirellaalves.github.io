# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.

def biggest_number(x, y):
    if x > y:
        return x
    else:
        return y


print(biggest_number(10, 11))
