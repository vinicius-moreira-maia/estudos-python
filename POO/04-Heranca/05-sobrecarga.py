# Sobrecarga de métodos em Python não existe. Em Java ou C++ se trata de criar métodos de mesmos nomes com assinaturas diferentes. O compilador saberá diferenciá-los de acordo com os valores de entrada.

'''
def x(a, b):
  return a + b

def x(a):
  return a + 1

# ERRO, a primeira função x perdeu sua referência para a segunda função.
# print(x(1, 2))

print(x(1))
'''

# é possível simular a sobrecarga com parâmetro default

def x(a, b = None):
  if b:
    return a + b
  return a + 1

# print(x(2, 2))
# print(x(2))

# usar '*' para múltiplos parâmetros é o melhor dos casos
# args é uma tupla / **kwargs seria um dicionário
def f(*args):
  if len(args) == 1:
    return args[0] + 1
  else:
    return args[0] + args[1]


print(f(2))
print(f(2, 2))