import re
import sys

# UM CRITÉRIO NÃO FOI SATISFEITO (em test_numb3rs.py)

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    try:
        n1, n2, n3, n4 = ip.split(".")
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)
        n4 = int(n4)
    except ValueError:
        return False

    if n1 in range(256) and n2 in range(256) and n3 in range(256) and n4 in range(256):
        return True
    else:
        return False

if __name__ == "__main__":
    main()