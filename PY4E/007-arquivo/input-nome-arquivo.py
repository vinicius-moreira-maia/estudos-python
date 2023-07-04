while True:
    try:
      n = input("Nome do arquivo: ")
      arquivo = open(n)
      break
    except FileNotFoundError:
      print("arquivo não existe")
      pass

i = 0
for line in arquivo:
    if line.startswith("Author"):
        i += 1

print(i)