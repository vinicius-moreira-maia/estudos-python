jogador = input("Nome: ")

# não precisa de break
match jogador:
    case "Messi" | "Neymar" | "Mbapé":
        print("PSG")
    case "Vini" | "Benzema":
        print("Real Madrid")
    case _: # tipo o 'else' ou o default de C
        print("Quem ?!")