arquivo = open("email.txt")

for line in arquivo:
    line = line.strip()
    if line.find('frankenstein') == -1:
        continue # pula a iteração
    print(line)

# find() procura a string passada como argumento em qualquer posição da linha e retorna -1 caso não a ache