def main():
    # dicionario com os casos base ja registrados
    d = {1:1, 2:2}

    print(fibo(36, d))
  

def fibo(n, d):
    '''retorna o n-ésimo número da sequência de fibonacci'''
    
    # se a resposta já tiver sido registrada
    if n in d:
        return d[n]
    
    # registrando as respostas (já que os dois casos recursivos irão repetir chamados com valores iguais)
    ans = fibo(n - 1, d) + fibo(n - 2, d)
    d[n] = ans

    return ans


if __name__ == "__main__":
    main()