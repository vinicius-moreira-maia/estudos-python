def main():
    num = get_num()
    miau(num)

def miau(n):
    for _ in range(n):
        print('miau')

def get_num():
    while True:
        n = int(input('Número: '))
        if n >= 0:
            return n
            
main()