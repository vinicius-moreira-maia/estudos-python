import inflect

p = inflect.engine()

def main():
    nomes = []

    while True:
        try:
            nome = input("Name: ")
        except EOFError:
            print()
            print("Adieu, adieu, to", pessoas)
            return 0 # retornar 0 significa que o programa encerrou sem erros

        nomes.append(nome)

        pessoas = p.join(nomes)

if __name__ == "__main__":
    main()