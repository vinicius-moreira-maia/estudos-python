nome = 'Vinicius Moreira Maia'
n = nome.split()
n2 = ''.join(n)
print(n2)

# histograma é um termo estatístico para um conjunto de frequências (frequência de cada letra no nome, no caso)
d = dict()

# otimização do laço usando o método get() -> mais sucinto!
for letra in n2:
    d[letra] = d.get(letra, 0) + 1

print(d)