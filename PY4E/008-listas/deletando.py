nomes = ["Camila", "Vinicius", "Thiago", "Zeno"]

# a partir do índice
# pop() modifica a lista e retorna o valor removido
x = nomes.pop(0)

print(x, nomes)

# deletando a partir do índice
del nomes[1]

print(nomes)

# a partir do valor
# remove() modifica a lista e não retorna o valor removido
z = nomes.remove("Zeno") 

print(nomes, z) # z é 'None'