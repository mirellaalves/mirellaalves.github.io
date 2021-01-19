# Exercício 14: O Fatorial de um número inteiro é representado pela
# multiplicação de todos os números predecessores maiores que 0.
# Por exemplo o fatorial de 5 é 120 pois 5! = 1 * 2 * 3 * 4 * 5 .
# Escreva um código que calcule o fatorial de um número inteiro.

n = 5

multiply = []
while n > 0:
    multiply.append(n)
    n = n - 1

print(multiply)

factorial = 1
for number in multiply:
    factorial = factorial * number

print(factorial)

# Exercício 16: Percorra a lista do exercício 14 e imprima
# "Múltiplo de 3" se o elemento for divisível por 3.

for number in multiply:
    if number % 3 == 0:
        print('Múltiplo de 3')
