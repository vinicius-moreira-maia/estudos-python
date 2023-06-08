def main():
    x = int(input("X: "))

    if for_par(x):
        print("par")
    else:
        print("ímpar")

def eh_par(x):
    return True if x % 2 == 0 else False # forma condensada do if

def for_par(x):
    return x % 2 == 0 # o resultado da comparação já é True ou False

main()