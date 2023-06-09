class Ordenador:
    def selection_sort(self, seq):
        fim = len(seq)

        for i in range(fim - 1):
            pos_do_menor = i

            # esse loop me garante que eu saiba a posição do menor elemento
            for j in range(i + 1, fim):
                if seq[j] < seq[pos_do_menor]:
                    pos_do_menor = j
            
            seq[i], seq[pos_do_menor] = seq[pos_do_menor], seq[i]  
    

    def bubble_sort(self, seq):
        ''' Implementação do curso da USP '''
        fim = len(seq)

        for i in range(fim - 1, 0, -1):
            for j in range(i):
                if seq[j] > seq[j + 1]:
                    seq[j], seq[j + 1] = seq[j+1], seq[j]
    

    def bubble(self, seq):
        ''' Implementação do programação Dinâmica '''
        fim = len(seq)

        for _ in range(fim - 1):
            for i in range(fim - 1):
                if seq[i] > seq[i + 1]:
                    seq[i], seq[i + 1] = seq[i+1], seq[i]
    

    def bubble_sort2(self, seq):
        ''' Implementação do curso da USP (versão melhorada) '''
        fim = len(seq)

        for i in range(fim - 1, 0, -1):
            trocou = False
            for j in range(i):
                if seq[j] > seq[j + 1]:
                    seq[j], seq[j + 1] = seq[j+1], seq[j]
                    trocou = True
            if not trocou:
               return


    def insertion_sort(self, lista):
        fim = len(lista)

        for i in range(1, fim):
            chave = lista[i]

            j = i - 1

            while j >= 0 and lista[j] > chave:
                lista[j + 1] = lista[j]
                j -= 1
            
            lista[j + 1] = chave
    
    
    def merge_sort(self, lista):
        ''' 
            diminuir a lista até o caso base (len(lista) == 1)
            intercalando as listas de 2 em 2
        '''

        # caso base
        if len(lista) <= 1:
            return lista
        
        meio = len(lista) // 2

        # ordenando as sublistas
        lado_esq = self.merge_sort(lista[:meio])
        lado_dir = self.merge_sort(lista[meio:])

        # intercalação
        return self.merge(lado_esq, lado_dir)


    def merge(self, lado_esq, lado_dir):
        if not lado_esq:
            return lado_dir
        
        if not lado_dir:
            return lado_esq

        if lado_esq[0] < lado_dir[0]:
            return [lado_esq[0]] + self.merge(lado_esq[1:], lado_dir)
        
        return [lado_dir[0]] + self.merge(lado_esq, lado_dir[1:])


if __name__ == '__main__':
    ...
