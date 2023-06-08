import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("To few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("To many command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")

    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(n_linhas(file))

def n_linhas(file):
    cont = 0
    for line in file:
        if not line.strip().startswith("#") and len(line.strip()) != 0:
            cont += 1
    return cont

if __name__ == "__main__":
    main()