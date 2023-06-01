def insertion_sort(lista):
    fim = len(lista)

    # começando do segundo
    for i in range(1, fim):
        chave = lista[i]
        
        # elemento imediatamente anterior ao elemento a ser ordenado
        j = i - 1

        # percorre-se a sublista de trás para frente, comparando o elemento a ser inserido com todos os outros, até achar sua posição correta
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        
        # j + 1, pois o j é decrementado pelo loop anterior e termina sempre uma posição antes da posição de inserir
        lista[j + 1] = chave

    return lista