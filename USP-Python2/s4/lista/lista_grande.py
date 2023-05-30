from random import randint

def lista_grande(n):
    l = []
    for _ in range(n):
        l += [randint(0, n)]
    
    return l

print(lista_grande(10))
