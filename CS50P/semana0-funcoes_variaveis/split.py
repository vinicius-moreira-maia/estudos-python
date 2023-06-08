s = "Vinicius Moreira Maia"
s2 = "Vinicius,Moreira,Maia"
nome1, nome2, nome3 = s.split() # no lado esquerdo da expressão é uma tupla!
y = s2.split(',') # o parâmetro é o separador / split retorna uma lista

print(y)

print(type(y))

print(f"Nome 1: {nome1}, Nome 2: {nome2}, Nome 3: {nome3} ")