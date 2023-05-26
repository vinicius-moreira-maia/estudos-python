def main():
    print(remove_repetidos([7,3,33,12,3,3,3,7,12,100]))

def remove_repetidos(lista):
    return sorted(list(set(lista[:])))
    
if __name__ == '__main__':
    main()