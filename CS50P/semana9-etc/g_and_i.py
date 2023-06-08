def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

# função geradora
def sheep(n):
    for i in range(n):
        yield "🐑" * i # no lugar de retornar tudo de uma vez (com return), yield retorna um valor por vez enquanto o loop for itera, sem encerrar a iteração (return encerra no primeiro retorno)

# o gerador 'yield' retorna um iterador, que é de fato iterado no laço da função main, e então pausa sua execução, quando o laço da função main termina de iterar, a função geradora retorna mais um 'pedaço' dos dados sempre guardando seu estado anterior

if __name__ == "__main__":
    main()