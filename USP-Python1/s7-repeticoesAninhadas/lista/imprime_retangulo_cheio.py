def main():
    larg = int(input('digite a largura: '))
    alt = int(input('digite a altura: '))
    print_rect(larg, alt)


def print_rect(larg, alt):
    i = 1
    while i <= alt:
        j = 1
        while j <= larg:
            print('#', end = '')
            j += 1
        i += 1
        print()


if __name__ == "__main__":
    main()