class Ordenador:
    def selection_sort(seq):
        fim = len(seq)
        cont = 0

        # -1 pois o último que sobrar não tem com o que ser comparado (já estará ordenado)
        for i in range(fim - 1):
            # o menor elemento visto, pra começar, é o i-ésimo
            pos_do_menor = i

            # comparando o resto da lista a partir da posição do 'menor' (i) + 1 (para não comparar o valor com ele mesmo) até o fim da lista
            for j in range(i + 1, fim):
                if seq[j] < seq[pos_do_menor]:
                    # o elemento na posição j passa a ser o menor
                    pos_do_menor = j
            
            # trocando
            if seq[pos_do_menor] == 2:
                cont += 1
            seq[i], seq[pos_do_menor] = seq[pos_do_menor], seq[i]  
        return cont



seq = [55,33,0,900,-432,10,77,2,11]
print(seq)

Ordenador.selection_sort(seq)
print(seq)

print(Ordenador.selection_sort(seq))