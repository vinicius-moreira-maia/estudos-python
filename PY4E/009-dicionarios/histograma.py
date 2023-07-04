nome = 'Vinicius Moreira Maia'
n = nome.split()
n2 = ''.join(n)
print(n2)

# histograma é um termo estatístico para um conjunto de frequências (frequência de cada letra no nome, no caso)
d = dict()
for letra in n2:
    if letra not in d:
        d[letra] = 1
    else:
        d[letra] += 1

print(d)