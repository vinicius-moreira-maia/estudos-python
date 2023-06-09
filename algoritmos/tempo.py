from ordenacao import Ordenador
import time
from busca import Busca

class Tempo:
    def compara(seq):
        '''
            O método time() do módulo time retorna quanto tempo (segundos) se 
            passou desde 1/1/1970 (data de criação do UNIX)

            --> Lembrar que tempo não é uma boa unidade de medida para analisar algoritmos, 
                pois leva em consideração tanto a implementação como a máquina. A forma 
                correta de analisar o tempo de execução é através de notação assintótica. 
        '''

        ord = Ordenador()

        seq1 = seq[:]
        seq2 = seq[:]
        seq3 = seq[:]
        seq4 = seq[:]

        print('----- ORDENAÇÃO -----')

        # Seleção 
        antes = time.time()
        ord.selection_sort(seq1)
        depois = time.time()
        
        print(f"Selection Sort demorou {depois - antes} segundos")

        # Bolha
        antes = time.time()
        ord.bubble(seq2)
        depois = time.time()
        
        print(f"Bubble Sort demorou {depois - antes} segundos")

        # Inserção
        antes = time.time()
        ord.insertion_sort(seq3)
        depois = time.time()
        
        print(f"Insertion Sort demorou {depois - antes} segundos")

        # Merge Sort
        antes = time.time()
        ord.merge_sort(seq4)
        depois = time.time()
        
        print(f"Merge Sort demorou {depois - antes} segundos")

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
