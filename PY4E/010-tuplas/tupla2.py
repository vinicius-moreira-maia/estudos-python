# Comparando tuplas: elemento por elemento é comparado, e o elemento subsequente não importa (mesmo que este seja muito grande)

n = 'Zé Vinicius Moreira Maia'
nomes  = n.split()

lista = []
for nome in nomes:
    lista.append((len(nome), nome))

print(lista)

# o método sort funciona dessa forma, elemento por elemento é comparado (reverse = True quer dizer que a ordem será decrescente)
lista.sort(reverse = True)

res = []

# ordenação dos nomes de forma decrescente
for tam, pal in lista:
    res.append(pal)

print(res)

