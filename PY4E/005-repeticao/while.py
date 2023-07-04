while True:
    line = input("> ")
    if line[0] == "#":
        continue # pula para a próxima iteração sem executar as próximas linhas
    if line == "pronto":
        break
    print(line)

print("Pronto!")