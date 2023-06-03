def soma_lista(lista):
      if len(lista) == 1:
          return lista[0]

      return lista[0] + soma_lista(lista[1:]) 
    

if __name__ == '__main__':
        print(soma_lista([3, 4, 3]))