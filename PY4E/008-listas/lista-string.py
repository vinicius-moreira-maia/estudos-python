nome = "Vinicius Moreira Maia"

# instancia uma lista com todos os caracteres da string 'nome'
t = list(nome)

print(t)
print(nome)

# omitindo o argumento, irá separar tendo como separador o espaço em branco
r = nome.split()
print(r)
print(nome)

# a primeira string é o separador
print(" ".join(r))