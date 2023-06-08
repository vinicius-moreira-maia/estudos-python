def main():
    print(f"Change Owed: {coke_machine()}")

def coke_machine():
    falta = 50
    while True:
        print(f"Amount Due: {falta}")
        d = int(input("Insert Coin: "))
        if d not in [25, 10, 5]:
            continue
        else:
            falta -= d
            if falta <= 0:
                return falta * -1

main()