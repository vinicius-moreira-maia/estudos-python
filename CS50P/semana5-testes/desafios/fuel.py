def main():
    f = input("Fraction: ").strip()
    p = gauge(convert(f))
    print(p)

# PRECISEI QUEBRAR ESSA FUNÇÃO TIRANDO O TRATAMENTO DE EXCEÇÕES ASSIM COMO OS REPROMPTS PARA NÃO GERAR CONFLITO NO PYTEST
def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    res = round(x / y * 100)
    return res

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()