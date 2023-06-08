import csv

nome = input("Nome: ")
bairro = input("Bairro: ")

with open("bairros.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["nome", "bairro"])
    writer.writerow({"nome" : nome, "bairro" : bairro})

print(type(writer)) # class csv.DictWriter
print(writer) # endereço de memória