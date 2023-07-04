# a maioria dos métodos de listas não retorna valores

x = [2, 4, 5, 77, 8, 1, 23]
x.append('doidoooooo')

print(x)

x2 = ['zé', 'ruela']

x.extend(x2)

print(x)

# a segunda lista não é modificada
print(x2)

x3 = x[:7]

# print(sorted(x3)) -> sorted por si só não  modifica a lista, POIS NÃO É UM MÉTODO DE LISTAS
x3 = sorted(x3)
print(x3) 
print(x)