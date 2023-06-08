import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    padrao1 = re.search(r"^\d{1,2}:\d\d (A|P)M to \d{1,2}:\d\d (A|P)M$", s)
    padrao2 = re.search(r"^\d\d? (A|P)M to \d\d? (A|P)M$", s)

    if not padrao1 and not padrao2:
        raise ValueError

    if not padrao1 == None:
        hora = padrao1.group().split()

        if not padrao1_valido(hora[0], hora[3]):
            raise ValueError
        else:
            return converte1(hora)

    if not padrao2 == None:
        hora = padrao2.group().split()

        if not padrao2_valido(hora[0], hora[3]):
            raise ValueError
        else:
            return converte2(hora)

def converte2(h):
    if h[1] == 'AM':
        hora1 = int(h[0])
    if h[1] == 'PM':
        hora1 = int(h[0]) + 12

    if h[4] == 'AM':
        hora2 = int(h[3])
    if h[4] == 'PM':
        hora2 = int(h[3])  + 12

    if hora1 > 10 and hora2 > 10:
        if hora1 == 12 and h[1] == "AM":
            hora1 = "00"
        if hora2 == 12 and h[4] == "AM":
            hora2 = "00"
        if hora1 == 24 and h[1] == "PM":
            hora1 = "12"
        if hora2 == 24 and h[4] == "PM":
            hora2 = "12"
        return f"{hora1}:00 to {hora2}:00"
    elif hora1 < 10 and hora2 > 10:
        if hora2 == 12 and h[4] == "AM":
            hora2 = "00"
        if hora2 == 24 and h[4] == "PM":
            hora2 = "12"
        return f"0{hora1}:00 to {hora2}:00"
    elif hora1 > 10 and hora2 < 10:
        if hora1 == 12 and h[1] == "AM":
            hora1 = "00"
        if hora1 == 24 and h[1] == "PM":
            hora1 = "12"
        return f"{hora1}:00 to 0{hora2}:00"
    else:
        return f"0{hora1}:00 to 0{hora2}:00"

def converte1(h):
    hora1, minuto1 = h[0].split(":")
    hora2, minuto2 = h[3].split(":")

    if h[1] == 'AM':
        hora1 = int(hora1)
    if h[1] == 'PM':
        hora1 = int(hora1) + 12

    if h[4] == 'AM':
        hora2 = int(hora2)
    if h[4] == 'PM':
        hora2 = int(hora2)  + 12

    if hora1 > 10 and hora2 > 10:
        if hora1 == 12 and h[1] == "AM":
            hora1 = "00"
        if hora2 == 12 and h[4] == "AM":
            hora2 = "00"
        if hora1 == 24 and h[1] == "PM":
            hora1 = "12"
        if hora2 == 24 and h[4] == "PM":
            hora2 = "12"
        return f"{hora1}:{minuto1} to {hora2}:{minuto2}"
    elif hora1 < 10 and hora2 > 10:
        if hora2 == 12 and h[4] == "AM":
            hora2 = "00"
        if hora2 == 24 and h[4] == "PM":
            hora2 = "12"
        return f"0{hora1}:{minuto1} to {hora2}:{minuto2}"
    elif hora1 > 10 and hora2 < 10:
        if hora1 == 12 and h[1] == "AM":
            hora1 = "00"
        if hora1 == 24 and h[1] == "PM":
            hora1 = "12"
        return f"{hora1}:{minuto1} to 0{hora2}:{minuto2}"
    else:
        return f"0{hora1}:00 to 0{hora2}:00"

def padrao1_valido(h1, h2):
    hora1, minuto1 = h1.split(":")
    hora2, minuto2 = h2.split(":")

    if int(hora1) > 12 or int(minuto1) > 59:
        return False
    elif int(hora2) > 12 or int(minuto2) > 59:
        return False
    else:
        return True

def padrao2_valido(h1, h2):
    if int(h1) > 12:
        return False
    elif int(h2) > 12:
        return False
    else:
        return True

if __name__ == "__main__":
    main()