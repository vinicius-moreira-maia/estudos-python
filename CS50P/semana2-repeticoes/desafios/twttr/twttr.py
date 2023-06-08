def main():
    s = input('Input: ')
    print(f"Output: {twttr(s)}")

def twttr(s):
    s = list(s)
    s2 = []
    for letra in s:
        if letra not in "aeiouAEIOU":
            s2.append(letra)
    return ''.join(s2)

main()