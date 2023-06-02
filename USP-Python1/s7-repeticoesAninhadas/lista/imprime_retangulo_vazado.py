def main():
    larg = int(input('digite a largura: '))
    alt = int(input('digite a altura: '))
    print_rect(larg, alt)


def print_rect(larg, alt):
    for i in range(1, alt + 1):
        if i == 1 or i == alt:
            print('#' * larg)
        else:
            print('#' + (' ' * (larg - 2)) + '#')
    

if __name__ == "__main__":
    main()