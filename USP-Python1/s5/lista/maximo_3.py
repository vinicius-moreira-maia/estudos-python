def maximo(a, b, c):
    maior = a
    
    for i in [a, b, c]:
        if i > maior:
            maior = i
    
    return maior