import csv

# O leitor define como dialeto padrão excel , que significa dizer que o
# delimitador de campos será a " , " e o caractere de citação será aspas
# duplas ( " ). Uma forma de modificar estes padrões é definindo-os de forma
# diferente na criação do leitor.

# header, *data é um truque para separarmos o cabeçalho do restante dos dados.
# Quando há uma atribuição múltipla e o valor da direita (beach_status_reader)
# pode ser percorrido, o Python entende que deve atribuir cada um dos valores
# a uma variável da esquerda (header, *data), seguindo a ordem. Isto é chamado
# de desempacotamento de valores. (VER arquivo try.py)

# lê os dados
with open("balneabilidade.csv") as file:
    beach_status_reader = csv.reader(file, delimiter=",", quotechar='"')
    header, *data = beach_status_reader

print(header)

# agrupa campanhas e suas respectivas balneabilidades
bathing_by_campaign = {}
for row in data:
    campaign = row[6]
    bathing = row[2]
    if campaign not in bathing_by_campaign:
        bathing_by_campaign[campaign] = {
            "Própria": 0,
            "Imprópria": 0,
            "Muito Boa": 0,
            "Indisponível": 0,
            "Satisfatória": 0,
        }
    bathing_by_campaign[campaign][bathing] += 1

# escreve o relatório em csv
# abre um arquivo para escrita
with open("report_por_campanha.csv", "w") as file:
    writer = csv.writer(file)

    # escreve o cabeçalho
    headers = [
        "Campanha",
        "Própria",
        "Imprópria",
        "Muito Boa",
        "Indisponível",
        "Satisfatória",
    ]
    writer.writerow(headers)

    # escreve as linhas de dados
    for campaign, bathing in bathing_by_campaign.items():
        # desempacota os valores de balneabilidade para formar uma linha
        # equivalente a
        # row = [campaign]
        # for value in bathing.values():
        #     row.append(value)
        row = [campaign, *bathing.values()]
        writer.writerow(row)


print(data[0])
