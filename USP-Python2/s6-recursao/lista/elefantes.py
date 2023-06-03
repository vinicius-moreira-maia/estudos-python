# a * b = a + a + a + a ... (b vezes)
# a * b = a + a(b - 1)

def incomodam(n):
    if n <= 0:
        return ''
    
    return 'incomodam ' + incomodam(n - 1)


# lembrar que, sempre que uma nova chamada é feita, a função é executada inteira, de cima pra baixo
# e nesse caso, os valores de retorno de uma função vão se somando (concatenando) uns com os outros
def elefantes(n):
    if n < 1:
        return ''
    elif n == 1:
        return 'Um elefante incomoda muita gente'
    elif n == 2:
        return elefantes(n - 1) + f'\n{n} elefantes incomodam incomodam muito mais'
    # as chamadas recursivas só começam quando n > 2
    elif n > 2:
        frase1 = f'\n{n - 1} elefantes incomodam muita gente'
        frase2 = f'\n{n} elefantes ' + f'{incomodam(n)}muito mais'
        return elefantes(n - 1) + frase1 + frase2 
    

if __name__ == '__main__':
    print(elefantes(4))