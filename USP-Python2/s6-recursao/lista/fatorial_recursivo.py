# Problemas que contém dentro de si problemas menores similares ao problema maior. Esses problemas tem uma estrutura recursiva.

# Se o problema for pequeno, resolva-o (caso base)

# Se o problema for grande, reduza-o (caso recursivo)
    # até chegar no caso base
    # depois volte à instância original

def fatorial(n):
    # caso base
    if n < 1:
        return 1
    
    # caso recursivo
    return n * fatorial(n - 1)
