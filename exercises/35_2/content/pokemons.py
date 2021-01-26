import json

# LOADS
# with open("pokemons.json") as file:
#     content = file.read()
#     pokemons = json.loads(content)["results"]  # o conteúdo é transformado em
#     # estrutura python equivalente, dicionário neste caso.
#     # acessamos a chave results que é onde contém nossa lista de pokemons

# LOAD
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]
    # loads - carrega o JSON a partir de um texto
    # load - carrega o JSON a partir de um arquivo

# Separamos somente os do tipo grama
grass_type_pokemons = [
    pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
]

# DUMPS
# Abre o arquivo para escrevermos apenas os pokemons do tipo grama
# with open("grass_pokemons.json", "w") as file:
#     json_to_write = json.dumps(
#         grass_type_pokemons
#     )  # conversão de Python para o formato json (str)
#     file.write(json_to_write)

# DUMP
with open("grass_pokemons.json", "w") as file:
    # escreve no arquivo já transformando em formato json a estrutura
    json.dump(grass_type_pokemons, file)

print(pokemons[0])  # imprime o primeiro pokemon da lista
