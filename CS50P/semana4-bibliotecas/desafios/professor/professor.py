import random

def main():
    pontos = 10
    level = get_level()
    problemas = 0

    while True:
        tentativas = 0
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        exp = str(num1) + " + " + str(num2) + " = "
        problemas += 1

        while True:
            try:
                res = int(input(exp))
                if res != num1 + num2:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("EEE")
                tentativas += 1
                pass

            if tentativas == 3:
                print(f"{exp}{num1 + num2}")
                pontos -= 1
                break

        if problemas == 10:
            print("Score:", pontos)
            return 0

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                raise ValueError
            else:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
