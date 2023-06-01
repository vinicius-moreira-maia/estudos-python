import random
from tempo import Tempo


def gera_lista(n):
        lista = []
        for _ in range(n):
            num = random.randint(-10, 10)
            lista.append(num)
    
        return lista

if __name__ == '__main__':
    lista = gera_lista(10000)
    Tempo.compara(lista)