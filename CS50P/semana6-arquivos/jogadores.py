import csv

jogadores = []
j = []

with open("jogadores.csv") as file:
        reader = csv.DictReader(file)
        for linha in reader:
            jogadores.append(linha)
            j.append({"nome": linha["nome"], "lugar": linha["lugar"]})

#print(jogadores)
#print(j)

'''def get_name(jogador):
    return jogador["nome"]'''

# usando uma função anônima (lambda) como chave de ordenação do dicionário
for jogador in sorted(jogadores, key = lambda jogador: jogador["nome"] ):
    print(f"{jogador['nome']} : {jogador['lugar']}")