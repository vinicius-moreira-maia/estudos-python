from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fontes = figlet.getFonts()

def main():

    # checagem de erros
    if len(sys.argv) not in [1, 3]:
        sys.exit("Invalid Usage")

    if len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in fontes:
            sys.exit("Invalid Usage")

    # caso nenhum argumento seja passado via CLI, a fonte será aleatória
    if len(sys.argv) == 1:
        rndm = True
    else:
        rndm = False

    frase = input("Input: ")

    print("Output: ")
    converte(frase, rndm)

def converte(frase, rndm):
    if not rndm:
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(frase))
    else:
        figlet.setFont(font = random.choice(fontes))
        print(figlet.renderText(frase))

if __name__ == "__main__":
    main()