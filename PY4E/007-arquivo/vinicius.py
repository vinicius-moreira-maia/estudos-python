arquivo = open("vinicius.txt")

# o método read() retorna uma string contendo todo o texto do arquivo
texto = arquivo.read()

# exibe o identificador do arquivo
print(arquivo)

i = 0
for line in arquivo:
    i += 1

print(f"linhas: {i}")

print(type(texto))