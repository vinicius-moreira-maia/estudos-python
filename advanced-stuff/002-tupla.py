import sys

# tuplas são menores que listas
lista = [2, 3, 44, 3, "xuxuzinho"]
tupla = (2, 3, 44, 3, "xuxuzinho")
print(sys.getsizeof(lista, "bytes"))
print(sys.getsizeof(tupla, "bytes"))

import timeit

# cada statement (stmt) será repetido 1 bilhão de vezes
# timeit retorna o tempo de execução
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1_000_000_000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1_000_000_000))