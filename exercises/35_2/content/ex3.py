# Exercício 3: Dado um arquivo contendo estudantes e suas respectivas notas,
# escreva um programa que lê todas essas informações e filtre somente as
# pessoas que estão aprovadas, escrevendo seus nomes em outro arquivo.
# A nota miníma para aprovação é 6.
# Arquivo:
#    Marcos 10
#    Felipe 4
#    José 6
#    Ana 10
#    Maria 9
#    Miguel 5
# Exemplo saída:
#    Marcos
#    José
#    Ana
#    Maria
# A função split pode ser utilizada para dividir o nome em uma linha.
# Ex: line.split() -> ["Marcos", "10"]
# Ex: line.split()[1] -> acessa o índice 1 - no exemplo acima, acessa "10".

file = open("ex3_file.txt")
new_file = open("ex3_new-file.txt", "w")

# reading = file.read()
# print(reading)

for line in file:
    if int(line.split()[1]) >= 6:
        new_file.write(f"{line.split()[0]}\n")
# mesmo que já haja conteúdo no arquivo "new_file", o .write sobrescreve.


file.close()
