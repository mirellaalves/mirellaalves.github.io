# Exercício 1: Faça um programa que receba um nome e imprima o mesmo na
# vertical em escada invertida. Exemplo:

# Entrada:
# PEDRO

# Saída:
# Copiar
# PEDRO
# PEDR
# PED
# PE
# P

name = input("Digite seu nome: ")


def print_name_vertical_inverted_ladder(name):
    name_len = len(name)

    while name_len > 0:
        print(name[:name_len])
        name_len = name_len - 1


print(print_name_vertical_inverted_ladder(name))

# RESPOSTA DO GABARITO:
# def vertical_inverted_ladder(word):
#     for removed_letters in range(len(word)):
#         for index in range(len(word) - removed_letters):
#             print(word[index], end="")
#         print()


# if __name__ == "__main__":
#     name = input("Digite um nome: ")
#     vertical_inverted_ladder(name)
