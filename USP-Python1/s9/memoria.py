# Objetos na Memória

x = [1, 2]
y = [1, 2]

# print(x[0] is y[0])

a = [2, 43, 4]

# b contém uma lista onde os 3 objetos apontam para a mesma lista, que é a
b = [a] * 3

print(b)

a.append('xuxu')

print(b)