import emoji

def main():
    frase = input("Input: ")
    print(emoji.emojize(frase, language = 'alias'))

if __name__ == "__main__":
    main()