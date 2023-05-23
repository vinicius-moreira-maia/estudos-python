# SEMPRE que eu escrever uma função, é importante escrever também um TESTE AUTOMATIZADO(uma função que testa outra) que verifica se a função está corretamente implementada. É basicamente chamar a função nas situações em que podem de fato ser problemáticas e verificar se o retorno é o esperado ou não.

# Lembrando que os módulos devem ser unidades testáveis! Para que o próprio teste possua valor.
   
def main():
    test_fat()

    n = int(input("n: "))
    k = int(input("k: "))
    
    print(f"o coeficiente binomial de n em k é: {coef_binomial(n, k)}")
    

def coef_binomial(n, k):
    '''
    Lembrando que k deve ser menor que n 
    '''
    return fat(n) // (fat(k) * fat(n - k))

def fat(x):
    if x == 1 or x == 0:
        return 1
    
    return x * fat(x - 1)

def test_fat():
    '''
    Função que testa os principais casos da função fat 
    '''

    print("Testing fat function.")

    if fat(0) == 1:
        print("    for 0 ok")
    else:
        print("    for 0 not ok")
    
    if fat(1) == 1:
        print("    for 1 ok")
    else:
        print("    for 1 not ok")
    
    if fat(2) == 2:
        print("    for 2 ok")
    else:
        print("    for 2 not ok")
    
    if fat(5) == 120:
        print("    for 5 ok")
    else:
        print("    for 5 not ok")
    
    print("End testing.\n")
        
if __name__ == "__main__":
    main()