x = [1, 3, 4, 2]
y = [23, 4, 777]
z = x + y # funciona como parece
w = y * 2 # funciona como parece

t = ['xuxu', 'xaxa', 'xexe']

# atualiza os valores da 'fatia' (slice) especificada
t[1:] = ['dudu', 'zé']
print(t)