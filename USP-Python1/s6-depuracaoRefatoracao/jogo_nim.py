def main():
    print()
    print('Bem-vindo ao jogo do NIM! Escolha:\n')
    print('1 - para jogar uma partida isolada')
    tipo = int(input('2 - para jogar um campeonato '))
    print()
    
    if tipo == 1:
        print('Você escolheu uma partida!')
        partida()
    if tipo == 2:
        print('Você escolheu uma campeonato!\n')
        campeonato()


def computador_escolhe_jogada(n, m):
    # lembrar que o operador '%' (módulo) tem precedência sobre adição e subtração
    if (n - 1) % (m + 1) == 0:
         return 1
    elif 2 <= m and (n - 2) % (m + 1) == 0:
         return 2
    else:
         if n - m < 0:
             return m - (m - n)
         else:
             return m


def usuario_escolhe_jogada(n, m):
    while True:
        n_pecas = int(input('Quantas peças você vai tirar? '))
        print()
        
        if n_pecas > m or n_pecas <= 0:
            print('Oops! Jogada inválida! Tente de novo.\n')
            continue
        else:
            return n_pecas


def partida():
    '''
        n é o número de peças
        m é o máximo de peças que podem ser retiradas
    '''
    print()
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    print()

    if n % (m + 1) == 0:
        print('Você começa!\n')

        while True:
            jogada_usuario = usuario_escolhe_jogada(n, m)
            n -= jogada_usuario
                
            if jogada_usuario == 1:
                print("Você tirou uma peça.")
            else:
                print(f"Você tirou {jogada_usuario} peças.")
            
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.\n')
            elif n > 1:
                print(f'Agora restam {n} peças no tabuleiro.\n')
            else:
                print('Fim do jogo! Você ganhou!\n')
                return True 
            
            jogada_pc = computador_escolhe_jogada(n, m)
            n -= jogada_pc
            
            if jogada_pc == 1:
                print("O computador tirou uma peça.")
            else:
                print(f"O computador tirou {jogada_pc} peças.")
            
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.\n')
            elif n > 1:
                print(f'Agora restam {n} peças no tabuleiro.\n')
            else:
                print('Fim do jogo! O Computador ganhou!\n')
                return False
    else:
        print('Computador começa!\n')
        
        while True:
            jogada_pc = computador_escolhe_jogada(n, m)
            n -= jogada_pc
            
            if jogada_pc == 1:
                print("O computador tirou uma peça.")
            else:
                print(f"O computador tirou {jogada_pc} peças.")
            
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.\n')
            elif n > 1:
                print(f'Agora restam {n} peças no tabuleiro.\n')
            else:
                print('Fim do jogo! O Computador ganhou!\n')
                return False

            jogada_usuario = usuario_escolhe_jogada(n, m)
            n -= jogada_usuario
                
            if jogada_usuario == 1:
                print("Você tirou uma peça.")
            else:
                print(f"Você tirou {jogada_usuario} peças.")
            
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.\n')
            elif n > 1:
                print(f'Agora restam {n} peças no tabuleiro.\n')
            else:
                print('Fim do jogo! Você ganhou!\n')
                return True


def campeonato():
    user = 0
    pc = 0

    for i in range(1, 4):
        print(f'**** Rodada {i} ****')

        if partida():
            user += 1
        else:
            pc += 1
    
    print('**** Final do campeonato! ****\n')
    print(f'Placar: Você {user} X {pc} Computador')
            

if __name__ == '__main__':
    main()