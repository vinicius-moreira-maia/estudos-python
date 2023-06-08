doces = {}

def main():
    while True:
        try:
            doce = input().strip().upper()
        except EOFError:
            break
        else:
            doces[doce] = doces.get(doce, 0) + 1

    lista_doces = list(doces.items())
    lista_doces.sort()

    for c, v in lista_doces:
        print(v, c)

main()