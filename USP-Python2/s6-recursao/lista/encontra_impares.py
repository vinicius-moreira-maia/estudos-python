def encontra_impares(lista):
    # Define a lista que armazenará os números ímpares
    lis = []

    # Verifica se há elementos na lista
    if len(lista) > 0:

        # Retira o primeiro elemento da lista
        # Aqui o problema será reduzido, em um momento não haverá mais elementos para verificar em 'lista' e essa condição (if len(lista) > 0) não será satisfeita
        numero = lista.pop(0)

        # Verifica se o número é ímpar
        if numero % 2 != 0:
            lis.append(numero)

        # Faz a união do resultado atual com o retorno para o resto da lista
        lis = lis + encontra_impares(lista)

    return lis
      

if __name__ == '__main__':
        print(encontra_impares([3, 4, 3, 8, 10, 2, 2]))