# atribuição à tuplas

m = ['oi', 'mundo']

x, y = m # tecnicamente na esquerda é uma tupla, mas os parênteses foram omitidos -> (x, y) = m
print(x, y)

# permutação 
a = 3
b = 7
print(f"a: {a}, b: {b}")
a, b = b, a # duas tuplas
print(f"a: {a}, b: {b}")

email = 'viniciusconcept@gmail.com'
usuario, dominio = email.split('@')
print(usuario, dominio) 