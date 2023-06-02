def main():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    print(soma_matrizes(m1, m2)) 


def dimensoes(matriz):
    '''
    i X j
    nº de listas X nº de elementos em cada lista
    '''
    i = len(matriz)
    j = len(matriz[0])
    return f'{i}X{j}'


def soma_matrizes(m1, m2):
    if dimensoes(m1) == dimensoes(m2):
        m3 = m1[:]

        for i in range(len(m3)):
            for j in range(len(m3[i])):
                m3[i][j] += m2[i][j]
        
        return m3
    else:
        return False


if __name__ == '__main__':
    main()