import sys

# Checagem de Erros
if len(sys.argv) < 2:
    sys.exit("poucos argumentos")

# slice
for arg in sys.argv[1:]:
    print(arg)