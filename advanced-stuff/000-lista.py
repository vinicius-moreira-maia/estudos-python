# objeto mutável

# 0 incluso, 21 não incluso, passo 2
lista = [x for x in range(0, 21, 2)] # comprehension

#print(lista)

lista2 = ["maçã", "banana", "laranja"]
lista3 = lista2 # lista3 aponta para o mesmo objeto que lista2 (alias)
lista2.append("xuxu")

#print(lista2)
#print(lista3)

#print(lista3.pop()) # exclui o último elemento e o retorna

#print(lista2)
#print(lista3)

lista4 = [0, 33, 1, 4, 5, 3, 2, -111]
#lista4.sort() # muta o objeto
#print(lista4)

lista5 = sorted(lista4) # retorna uma cópia da lista (não é método de lista)
#print(lista5) # cópia
#print(lista4) # original

# concatenação
#print([3] * 4)
#print([2, 3] + [1 + 1] + [0,[0,2]])

lista6 = [1, 2, 3, 4, 5]
lista7 = lista6[1:3] # terceiro elemento não incluso (retorna cópia)
#lista8 = lista6[::2] # passo 2
lista8 = lista6[::-1] # passo -1 (reverte a lista)
#print(lista7)
#print(lista8)

# copiando listas
lista8 = [2, 33, 22, 1]
print(f"{lista8} - {id(lista8)}")
print(f"{lista8.copy()} - {id(lista8.copy())}")

# estes 2 são os mesmos objetos (?)
print(f"{list(lista8)} - {id(list(lista8))}")
print(f"{lista8[:]} - {id(lista8[:])}")






