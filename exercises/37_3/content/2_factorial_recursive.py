'''
Nessa função acontece, "por baixo dos panos", a mesma coisa que a função do
exemplo anterior. Porém, explicando com outras palavras, internamente cada
chamada recursiva à função adiciona um frame de pilha, até chegarmos ao caso
base. Então, a pilha começa a se desenrolar à medida que cada chamada retorna
seus resultados.
'''


def factorial_recursive(n):  # nome da função e parâmetro
    if n == 1:  # condição de parada
        return 1

    else:
        return n * factorial_recursive(n - 1)  # chamada de si mesma com um
        # novo valor


print(factorial_recursive(5))
