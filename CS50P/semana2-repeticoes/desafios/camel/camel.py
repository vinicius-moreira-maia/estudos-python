def main():
    cc = input('camelCase: ')
    print(f"snake_case: {snake(cc)}")

def snake(s):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = s[i].lower()
            s.insert(i, "_")
    return ''.join(s)

main()
