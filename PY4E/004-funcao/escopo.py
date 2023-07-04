def main():
    x = 5

    # uma cópia de x é enviada (passagem por valor)
    print(vezes2(x))
    
    # x continua sendo 5
    print(x)

def vezes2(x):
    return x * 2

main()