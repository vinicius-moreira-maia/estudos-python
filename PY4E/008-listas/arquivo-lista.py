import re

horas = []

file = open("ex-arquivo.txt")
manha = 0

for line in file:

    # se a linha não começar com a string que me interessa, pulo para a próxima iteração, evitando, com isso, processar comandos desnecessários
    if not line.startswith("Date"):
        continue
    else:
        hora = re.findall("[0-9]{2}:[0-9]{2}:[0-9]{2}", line) 
        h = int(hora[0][:2])
        if h >= 5 and h <= 12: 
           manha += 1

print(f'Mensagens enviadas pela manhã: {manha}')

file.close()
