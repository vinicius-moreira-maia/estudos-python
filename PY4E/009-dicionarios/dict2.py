frutas = {'banana' : 4, 'maçã' : 5 , 'abacate' : 55}

# o método de dicionários 'values()' retorna os valores do dicionário, e a função 'list()' transforma esses valores em uma lista
qtd = list(frutas.values())

# Em listas, o operador in faz uso de busca linear (tempo linear O(n)), em dicionários, a busca é através de uma 'hash function' (hash table), portanto o tempo de busca é bem melhor em dicionários que em listas.
print(5 in qtd)