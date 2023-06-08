import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) == 1:
        sys.exit("To few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("To many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    reader = csv.DictReader(file)

    lista = []

    for line in reader:
        lista.append(line)

    print(tabulate(lista, headers = "keys", tablefmt = "grid"))

if __name__ == "__main__":
    main()