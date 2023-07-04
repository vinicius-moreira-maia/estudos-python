def main():
   x = [1, 2, 3, 4, 5, 6, 7]
   
   print(x)

   remove_impar(x)

   # x é alterado pela função, mesmo que seja um objeto local de main (passagem por referência!)
   print(x)

def remove_impar(y):
    cont = 0
    
    # quantidade de ímpares na lista
    for n in y:
        if n % 2 != 0:
            cont += 1

    i = 0
    cont2 = 0

    while True:
        if y[i] % 2 != 0:
            del y[i]
            cont2 += 1
        i += 1
        if cont == cont2:
            break

main()