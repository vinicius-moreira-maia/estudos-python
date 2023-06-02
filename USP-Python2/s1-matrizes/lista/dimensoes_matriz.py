def main():
    minha_matriz = [[1], [2], [3]]
    dimensoes(minha_matriz)

    minha_matriz = [[1, 2, 3], [4, 5, 6]]
    dimensoes(minha_matriz)


def dimensoes(matriz):
    '''
    i X j
    nº de listas X nº de elementos em cada lista
    '''
    i = len(matriz)
    j = len(matriz[0])
    print(f'{i}X{j}')


if __name__ == '__main__':
    main()