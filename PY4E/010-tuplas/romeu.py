import string

arquivo = open('texto.txt')

# criando o dicionário de frequências (histograma)
cont = {}
for linha in arquivo:
    linha = linha.lower().strip()
    linha = linha.translate(linha.maketrans('', '', string.punctuation))
    palavras = linha.split()
    for palavra in palavras:
        cont[palavra] = cont.get(palavra, 0) + 1

# transferindo os pares chave-valor para tuplas valor-chave contidas numa lista
l = []
for chave, valor in list(cont.items()):
   l.append((valor, chave))

# já que a ordem do par foi invertida, o método sort() compara primeiro o valor inteiro e, caso haja outro par com o mesmo valor, a ordenação será a partir do segundo elemento que é uma string
l.sort(reverse = True)
for valor, chave in l[:5]:
    print(f"{chave} : {valor}") 
