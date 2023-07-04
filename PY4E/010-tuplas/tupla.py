# tuplas = listas imutáveis - Podem ou não conter parênteses () envolvendo a coleção
x = (12, 3, 4, 5)
print(type(x))

# tupla de um elemento
y = (7,)
print(type(y))

# função construtora (cria uma tupla com os caracteres separados)
t = tuple('banana')
print(t)
print(type(t))

print(t[1])
print(t[1:3])

# erro
# t[0] = 'ty' -> assim como strings, não posso modificar o valor de uma tupla, mas posso sobrepor com outro objeto