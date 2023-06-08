import argparse

parser = argparse.ArgumentParser(description = "Meow like a cat")

# estou dando significado à string '-n' (número de vezes) -> flag, switch
parser.add_argument("-n", default = 1, help = "number of times to meow", type = int) # já faz a converção de tipo de str para int automaticamente
parser.add_argument("--name", default = "Vini", help = "names", type = str)

args = parser.parse_args()

print(args) # Namespace(...)
print(type(args))

for _ in range(args.n):
    print("meow")

print(args.name)