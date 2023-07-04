maximo = None
lista = [2, 43, 5, 6, -1, -2, 3, 4, -6]

for n in lista:
    print(f"Máximo: {maximo} / Número Atual: {n}")
    if maximo is None or n > maximo:
        maximo = n

print(f"Máximo final >>> {maximo}")
print(f"Máximo função >>> {max(lista)}")
