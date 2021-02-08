'''
Declaramos uma função com um parâmetro. Dentro da função criada, definimos
qual é a condição de parada da função. A condição de parada faz uma comparação
entre o valor da condição com o parâmetro que a função está recebendo. Caso a
condição não se satisfaça, a função a chamada novamente com um novo parâmetro.
Caso contrário a execução para na condição de parada.
'''


def countdown(n):  # nome da função e parâmetro
    if n == 0:  # condição de parada => CASO BASE: tipo a situação em que a
        # função já chega resolvida
        print('FIM!')
    else:
        print(n)
        countdown(n - 1)  # chamada de si mesma com um novo valor


countdown(5)
