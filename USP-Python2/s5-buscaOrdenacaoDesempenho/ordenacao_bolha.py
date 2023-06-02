import time
import random

# Comparação dos tempos de execução dos algoritmos de ordenação

class Ordenador:
    def selection_sort(seq):
        fim = len(seq)

        for i in range(fim - 1):
            pos_do_menor = i

            for j in range(i + 1, fim):
                if seq[j] < seq[pos_do_menor]:
                    pos_do_menor = j
            
            seq[i], seq[pos_do_menor] = seq[pos_do_menor], seq[i]  
    

    def bubble_sort(seq):
        fim = len(seq)

        # percorrendo ao contrário para ir definindo as "sublistas" a serem usadas no segundo for
        for i in range(fim - 1, 0, -1):
            for j in range(i):
                if seq[j] > seq[j + 1]:
                    seq[j], seq[j + 1] = seq[j+1], seq[j]
    

    def bubble_sort2(seq):
        fim = len(seq)

        for i in range(fim - 1, 0, -1):
            trocou = False
            # se em uma iteração não houver troca, posso parar de comparar, a lista estará ordenada
            for j in range(i):
                if seq[j] > seq[j + 1]:
                    seq[j], seq[j + 1] = seq[j+1], seq[j]
                    trocou = True
            if not trocou:
               return


class Tempo:
    def gera_lista(n):
        lista = []
        for _ in range(n):
            num = random.randint(-10, 10)
            lista.append(num)
    
        return lista
    

    def compara(seq):
        '''
            O método time() do módulo time retorna quanto tempo (segundos) se passou desde 1/1/1970 (data de criação do UNIX)
        '''

        seq1 = seq[:]
        seq2 = seq[:]
        seq3 = seq[:]

        # Seleção Direta
        antes = time.time()
        Ordenador.selection_sort(seq1)
        depois = time.time()
        
        print(f"Selection Sort demorou {depois - antes} segundos")

        # Bolha
        antes = time.time()
        Ordenador.bubble_sort(seq2)
        depois = time.time()
        
        print(f"Bubble Sort demorou {depois - antes} segundos")

        # Bolha Melhorada
        antes = time.time()
        Ordenador.bubble_sort2(seq3)
        depois = time.time()
        
        print(f"Bubble Sort >MELHORADA< demorou {depois - antes} segundos")


if __name__ == '__main__':
    seq = Tempo.gera_lista(10000)
    Tempo.compara(seq)
