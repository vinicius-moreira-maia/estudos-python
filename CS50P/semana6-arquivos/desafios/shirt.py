from PIL import Image, ImageOps
import sys
import os

def main():

    # Lidando com os argumentos da CLI
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    nome1, extensao1 = os.path.splitext(sys.argv[1].lower())
    nome2, extensao2 = os.path.splitext(sys.argv[2].lower())

    if extensao1 not in [".jpg", ".jpeg", ".png"]:
            sys.exit("Invalid input")

    if extensao2 not in [".jpg", ".jpeg", ".png"]:
            sys.exit("Invalid input")

    if extensao1 != extensao2:
        sys.exit("Input and output have different extensions")

    # Processamento de imagens
    try:
        blusa = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("File does not exist")

    tam_blusa = blusa.size

    try:
        foto = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    foto_alterada = ImageOps.fit(foto, tam_blusa)

    foto_alterada.paste(blusa, blusa)

    foto_alterada.save(sys.argv[2])

if __name__ == "__main__":
    main()