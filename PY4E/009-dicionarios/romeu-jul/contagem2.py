import string

nome_arq = input('Nome do arquivo: ')

try:
    arq = open(nome_arq)
except:
    print("Nome inválido!")
    exit()

cont = {}

# criando o dicionário
for linha in arq:
    linha = linha.strip().lower()
    linha = linha.translate(linha.maketrans('', '', string.punctuation))
    palavras = linha.split()
    for palavra in palavras:
        if palavra not in cont:
            cont[palavra] = 1
        else:
            cont[palavra] += 1

chaves = list(cont.keys())
chaves.sort()

# mostrando os itens em ordem alfabética
for chave in chaves:
    print(chave, cont[chave])

arq.close()