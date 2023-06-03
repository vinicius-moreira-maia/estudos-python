def fibonacci(n):
    ''' retorna o n-ésimo número da sequência '''

    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
