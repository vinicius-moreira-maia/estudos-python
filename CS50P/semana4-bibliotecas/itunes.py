import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

resposta = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])
print(type(resposta)) # requests.models.Response

# print(json.dumps(resposta.json(), indent = 2))

# o dicionario (json convertido) atribuído ao objeto 'saida'
saida = resposta.json()
print(type(saida)) # dict

# iterando na chave 'results' (que é uma lista de dicionários, 1 para cada música) do dicionário
for result in saida["results"]:
    print(result["trackName"])
