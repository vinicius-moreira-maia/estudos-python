def merge_sort(lista):
    ''' 
        diminuir a lista até o caso base (len(lista) == 1)
        intercalando as listas de 2 em 2
    '''

    # caso base
    if len(lista) <= 1:
        return lista
    
    meio = len(lista) // 2

    # ordenando as sublistas
    lado_esq = merge_sort(lista[:meio])
    lado_dir = merge_sort(lista[meio:])

    # intercalação
    return merge(lado_esq, lado_dir)


def merge(lado_esq, lado_dir):
    if not lado_esq:
        return lado_dir
    
    if not lado_dir:
        return lado_esq

    if lado_esq[0] < lado_dir[0]:
        return [lado_esq[0]] + merge(lado_esq[1:], lado_dir)
    
    return [lado_dir[0]] + merge(lado_esq, lado_dir[1:])

a = [3, 43, 2, 12, 9, 20, -2, 48, 0, -12, -2222, 12, 0.5647]

print(merge_sort(a))