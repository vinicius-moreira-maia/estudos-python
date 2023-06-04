import pytest

def busca_binaria_rec(lista, elemento, min=0, max=None):
    ''' max e min são parâmetros opcionais para definir uma sublista, se eu quiser '''

    # definindo maximo e minimo (sublistas)
    if max == None:
        max = len(lista) - 1
    
    if max < min: # caso base
        return False 
    else:
        meio = min + (max-min)//2
    
    if lista[meio] > elemento:
        return busca_binaria_rec(lista, elemento, min, meio - 1)
    elif lista[meio] < elemento:
        return busca_binaria_rec(lista, elemento, meio + 1, max)
    else:
        return meio

lista = [10, 20, 30, 50, 100, 300, 330, 400]

# parametrização dos testes
@pytest.mark.parametrize("lista, valor, esperado", [
    (lista, 10, 0),
    (lista, 300, 5),
    (lista, 3000, False)])

def testa_busca_binaria(lista, valor, esperado):
    assert busca_binaria_rec(lista, valor) == esperado

