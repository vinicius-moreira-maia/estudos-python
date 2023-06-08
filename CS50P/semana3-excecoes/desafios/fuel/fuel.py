def main():
    print(float_to_perc(get_fraction()))

def get_fraction():
    while True:
        f = input("Fraction: ").strip()
        try:
            x, y = f.split("/")
            if '/' not in f or int(x) > int(y):
                raise ValueError
            return int(x) / int(y)
        except (ValueError, ZeroDivisionError, IndexError):
            pass

def float_to_perc(n):
    n = round(n * 100)
    if n <= 1:
        return "E"
    elif n >= 99:
        return "F"
    else:
        return str(n) + "%"

main()