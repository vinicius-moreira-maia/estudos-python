def main():
    altura = int(input('Altura: '))
    cria_bloco(altura)

def cria_bloco(h):
    for _ in range(h): # linha
        for _ in range(h): # coluna
            print('#', end = '')
        print() # somente aqui a linha será pulada

main()
