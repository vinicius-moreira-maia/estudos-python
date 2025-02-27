# lista imutável

tupla1 = 2, 3, 5, 4 # parêntese opcional aqui
print(tupla1)

#print(type(("oi"))) # string
#print(type(("oi",))) # tupla
#print(type((None,))) # tupla

# copiando tuplas
#print(type(tupla1[:]))

# unpacking
a1, *a2, a3 = (33, 4, 22, 5, 6, 4)
print(a1)
print(a2) # todos os elementos intermediários como lista
print(a3)

