class Busca:
    def busca_sequencial(seq, x):
        for i in range(len(seq)):
            if seq[i] == x:
                return i
        return -1
    
    
    def busca_binaria(seq, x):
        primeiro = 0
        ultimo = len(seq) - 1

        # repetir até não existir mais sublista, ou seja, quando o primeiro passar a ser maior
        while primeiro <= ultimo:
            # '//' para caso a lista seja de tamanho ímpar
            meio = (primeiro + ultimo) // 2

            if seq[meio] == x:
                return meio
            else:
                if x < seq[meio]:
                    ultimo = meio - 1
                else: # if x > seq[meio]
                    primeiro = meio + 1
        
        return -1