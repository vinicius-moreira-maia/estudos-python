class Busca:
    def busca_sequencial(seq, x):
        for i in range(len(seq)):
            if seq[i] == x:
                return True
        return False


if __name__ == '__main__':
    seq = [0.4, 0.3, 1.33, 4.52]
    print(Busca.busca_sequencial(seq, 1.33))