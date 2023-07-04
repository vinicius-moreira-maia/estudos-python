nome_arq = input('Nome do arquivo: ')

try:
    arq = open(nome_arq)
except:
    print("Nome inválido!")
    exit()

cont = {}

# criando o dicionário
for linha in arq:
    palavras = linha.split()
    for palavra in palavras:
        cont[palavra] = cont.get(palavra, 0) + 1

chaves = list(cont.keys())
chaves.sort()

# mostrando os itens em ordem alfabética
for chave in chaves:
    print(chave, cont[chave])

# print(cont)
arq.close()