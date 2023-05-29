def main():
    print(menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']))
    print(menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']))

def menor_nome(nomes):
    nome_menor = nomes[0].strip().capitalize()
    
    for nome in nomes:
        if len(nome.strip()) < len(nome_menor):
            nome_menor = nome.strip().capitalize()
    
    return nome_menor

if __name__ == '__main__':
    main()