# Exercício 6: Crie uma função que receba os três lado de um triângulo e
# informe qual o tipo de triângulo formado ou "não é triangulo" ,
# caso não seja possível formar um triângulo.
# Dica:
#   Três lados formam um triângulo quando a soma de quaisquer dois lados for
# maior que o terceiro;
#   Triângulo Equilátero: três lados iguais;
#   Triângulo Isósceles: quaisquer dois lados iguais;
#   Triângulo Escaleno: três lados diferentes.


def triangle_type(side_one, side_two, side_three):
    if (
        side_one + side_two <= side_three or
        side_one + side_three <= side_two or
        side_two + side_three <= side_one
    ):
        return "Não é triângulo"
    elif side_one == side_two == side_three:
        return "Triângulo Equilátero"
    elif side_one != side_two != side_three:
        return "Triângulo Escaleno"
    else:
        return "Triângulo Isósceles"


print(triangle_type(3, 4, 5))

# Correção sobre conceito de triângulo:
# SILVA, Luiz Paulo Moreira. "O que é a condição de existência de um
# triângulo?"; Brasil Escola. Disponível em:
# https://brasilescola.uol.com.br/o-que-e/matematica/o-que-e-a-condicao-existencia-um-triangulo.htm.
# Acesso em 19 de janeiro de 2021.
