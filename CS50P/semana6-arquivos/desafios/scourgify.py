import sys
import csv

def main():

    lista = []

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    try:
        with open(sys.argv[1]) as input_file:
            reader = csv.DictReader(input_file)
            for line in reader:
                lista.append(line)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as output_file:
        writer = csv.DictWriter(output_file, fieldnames = ["first", "last", "house"])
        writer.writeheader()
        for line in lista:
            last, first = line["name"].split(",")
            writer.writerow({"first": first.strip(), "last": last.strip(), "house": line["house"]})

if __name__ == "__main__":
    main()