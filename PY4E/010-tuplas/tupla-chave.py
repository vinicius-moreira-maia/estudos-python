diretorio = {}
primeiro = 'Vini'
ultimo = 'Maia'

# tupla como chave
diretorio[primeiro, ultimo] = '3222-2224'

for primeiro, ultimo in diretorio:
    print(primeiro, ultimo, diretorio[primeiro, ultimo])

# chave de dicionario deve ser um tipo imutavel! (tupla ou string)