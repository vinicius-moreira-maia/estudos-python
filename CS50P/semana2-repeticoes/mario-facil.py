# Utilizando função para abstrair ações

def main():
    desenha_bloco(6)

def desenha_bloco(h):
    for _ in range(h):
        cria_tijolos(h)

def cria_tijolos(largura):
    print('#' * largura)

main()