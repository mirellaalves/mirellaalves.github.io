# Exercício 1: Faça um programa que solicite o nome de uma pessoa usuária e
# imprima-o na vertical. Exemplo:
# F
# U
# L
# A
# N
# O


name = input("Digite seu nome: ")


def print_name_vertical(name):
    for letter in name:
        print(letter)


print(print_name_vertical(name))
