x = {'banana': 30, 'ata': 500, 'abacaxi' : 14, 'melancia' : 3}

'''
y = {}

# só x.items() (sem list()) retorna um objeto da classe <dict_items>
y = list(x.items())

print(y)
y.sort()
print(y)
'''

# múltipla atribuição
l = list()
for chave, valor in list(x.items()):
    l.append((valor, chave))

l.sort(reverse = True)

print(l)