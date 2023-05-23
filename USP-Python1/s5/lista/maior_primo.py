def eh_primo(n):
    cont_divisores = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            cont_divisores += 1
    
    if cont_divisores == 2:
        return True
    else:
        return False

def maior_primo(n):
    maior = 0

    for i in range(1, n + 1):
        if eh_primo(i) and i > maior:
            maior = i
    
    return maior