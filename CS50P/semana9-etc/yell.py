def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words)
    print(type(uppercased))
    print(*uppercased)

if __name__ == "__main__":
    main()