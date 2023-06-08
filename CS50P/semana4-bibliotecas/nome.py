import sys

# Checagem de Erros
if len(sys.argv) < 2:
    sys.exit("poucos argumentos")
elif len(sys.argv) > 2:
    sys.exit("muitos argumentos")

print("Oi", sys.argv[1])