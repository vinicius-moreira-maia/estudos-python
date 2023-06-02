def ordenada(seq):
    fim = len(seq)
    cont = 0

    for i in range(fim - 1):
        pos_do_menor = i

        for j in range(i + 1, fim):
            if seq[j] < seq[pos_do_menor]:
                cont += 1
                pos_do_menor = j
        
        # trocando
        seq[i], seq[pos_do_menor] = seq[pos_do_menor], seq[i]  

    if cont == 0:
        return True
    else:
        return False

seq = [-1, 0.4, 2, 5, 55, 102]
print(ordenada(seq))