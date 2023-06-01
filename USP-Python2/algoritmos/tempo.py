from ordenacao import Ordenador
import time
from busca import Busca

class Tempo:
    def compara(seq):
        '''
            O método time() do módulo time retorna quanto tempo (segundos) se passou desde 1/1/1970 (data de criação do UNIX)
        '''

        seq1 = seq[:]
        seq2 = seq[:]
        seq3 = seq[:]

        print('----- ORDENAÇÃO -----')

        # Seleção 
        antes = time.time()
        Ordenador.selection_sort(seq1)
        depois = time.time()
        
        print(f"Selection Sort demorou {depois - antes} segundos")

        # Bolha
        antes = time.time()
        Ordenador.bubble(seq2)
        depois = time.time()
        
        print(f"Bubble Sort demorou {depois - antes} segundos")

        # Inserção
        antes = time.time()
        Ordenador.insertion_sort(seq3)
        depois = time.time()
        
        print(f"Insertion Sort demorou {depois - antes} segundos")

        print('\n----- BUSCA -----')

        # Busca Linear
        antes = time.time()
        print("índice:", Busca.busca_sequencial(seq3, 0))
        depois = time.time()
        
        print(f"Busca Linear demorou {depois - antes} segundos")

        # Busca Binária
        antes = time.time()
        print("índice:", Busca.busca_binaria(seq3, 0))
        depois = time.time()
        
        print(f"Busca Binária demorou {depois - antes} segundos")
