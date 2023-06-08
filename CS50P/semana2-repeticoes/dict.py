# lista de dicionários
jogadores = [
    {'nome' : 'Cristiano Ronaldo', 'gols': 807},
    {'nome' : 'Lionel Messi', 'gols': 758},
    {'nome' : 'Pelé', 'gols': 757},
    {'nome' : 'Romário', 'gols': 747}
]

for jogador in jogadores:
    print(jogador['nome'],  jogador['gols'], sep = ", ")