def main():
    print(f"Output: {twttr(input('Input: '))}")

def shorten(s):
    s = list(s)
    s2 = []
    for letra in s:
        if letra not in "aeiouAEIOU":
            s2.append(letra)
    return ''.join(s2)

if __name__ == "__main__":
    main()