import re
import sys

def main():
    print(count(input("Text: ").strip()))

def count(s):
    # checando pra ver se 'um' está, simultaneamente, no começo e no fim de uma palavra, que no caso é o próprio 'um'
    x = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(x)

if __name__ == "__main__":
    main()