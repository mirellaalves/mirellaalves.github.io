'''
Exercício 1 Em um software monitor, que verifica a resiliência de outro
software, precisamos saber qual o tempo máximo que um software permaneceu sem
instabilidades. Para isto, a cada hora é feito uma requisição ao sistema e
verificamos se está ok. Supondo um array que contenha os estados coletados por
nosso software, calcule quanto tempo máximo que o servidor permaneceu sem
instabilidades.

1 - OK
0 - Instabilidades

valores_coletados = [0, 1, 1, 1, 0, 0, 1, 1]
resultado = 3

valores_coletados = [1, 1, 1, 1, 0, 0, 1, 1]
resultado = 4
'''


def max_time_without_instabilities(data):
    for item in data:
        pass
