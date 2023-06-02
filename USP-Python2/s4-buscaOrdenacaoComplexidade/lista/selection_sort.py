def ordena(seq):
    fim = len(seq)

    for i in range(fim - 1):
        pos_do_menor = i

        for j in range(i + 1, fim):
            if seq[j] < seq[pos_do_menor]:
                pos_do_menor = j
        
        # trocando
        seq[i], seq[pos_do_menor] = seq[pos_do_menor], seq[i]  
    
    return seq