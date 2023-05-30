class Busca:
    def busca_sequencial(seq, x):
        '''(list, float) -> bool'''
        for i in range(len(seq)):
            if seq[i] == x:
                return True
        return False

seq = [0.4, 0.3, 1.33, 4.52]

print(Busca.busca_sequencial(seq, 1.33))