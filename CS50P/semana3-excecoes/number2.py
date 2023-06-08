def main():
    x = get_int("x: ")
    print(f"X é {x}")

def get_int(prompt):
    # enquanto der erro não sairá do loop
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            # print("x não é inteiro")
            pass

main()