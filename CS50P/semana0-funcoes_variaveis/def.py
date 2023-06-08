def main():
    n = input("Nome: ").strip().title()
    oi()
    oi(n)

def oi(n = "mundo"):
    print(f"Oi, {n}!")

main()