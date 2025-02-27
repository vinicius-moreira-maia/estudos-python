dicionario = {"banana": 3,
              "maçã": 10,
              "xuxu": 2}

# nenhum desses métodos retornam listas ou tuplas
# retornam objetos de visuzalização
# são iteráveis, mas não indexáveis
#print(dicionario.keys())
#print(dicionario.values())
#print(dicionario.items())

#print(dicionario.keys()[0])
#print(list(dicionario.keys())[0])

# cada elemento do retorno de items() é uma tupla
#for k, v in dicionario.items(): # unpacking
    #print(k, v)

# excluindo elementos
#del dicionario["xuxu"]
#print(dicionario.pop("xuxu")) # retorna o valor da chave
#dicionario.popitem() # remove o último elemento inserido

#print(dicionario)

# no lugar de dar KeyError retorna None, caso não haja o elemento
#print(dicionario.get("mamão"))

# copiando dicionários
dicionario2 = {"banana": 3,
              "maçã": 10,
              "xuxu": 2}

#print(id(dicionario2))
#print(id(dicionario2.copy()))
#print(id(dict(dicionario2)))

dicionario3 = {"nome": "Zé",
              "cidade": "Icó",
              "idade": 22,
              "email": "zeh@hotmail"}
dicionario4 = dict(nome="Zunim", cidade="Assú", idade=44)

# sobrepõe as chaves iguais e adiciona as novas
dicionario4.update(dicionario3)

print(dicionario4)

# qualquer elemento imutável pode ser chave
# "todo objeto que pode ser chave de dicionário ou estar em um set é um objeto hashable" (geralmente objetos imutáveis, mas não é regra)
print({hash("xuxu"): 33,
       (22,): 23})

