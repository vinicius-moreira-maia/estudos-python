nomes = []

with open("names.txt") as file:
    print(file)
    for line in file:
        nomes.append(line.strip())

for nome in sorted(nomes):
    print("oi", nome)
