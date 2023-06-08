def main():
    h = input("What time is it? ")
    hora_comida = convert(h)

    if 7 <= hora_comida <= 8:
        print("breakfast time")
    elif 12 <= hora_comida <= 13:
        print("lunch time")
    elif 18 <= hora_comida <= 19:
        print("dinner time")

def convert(time):
    h, m = time.split(":")
    h = float(h)
    m = float(m) / 60

    return h + m

if __name__ == "__main__":
    main()
