def main():
    print(maiusculas('Programamos em python 2?'))
    print(maiusculas('PrOgRaMaMoS em python!'))


def maiusculas(frase):
    res = ''

    for letra in frase:
        if letra.isupper():
            res += letra
    
    return res


if __name__ == '__main__':
    main()