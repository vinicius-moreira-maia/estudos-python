def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    num = False
    for l in s:
        if l.isdigit():
            num = True
            break
    if num:
        if comeca_com_2letras(s) and tamanho_valido(s) and numeros_corretos(s) and caracteres_corretos(s):
            return True
        else:
            return False
    else:
        if comeca_com_2letras(s) and tamanho_valido(s) and caracteres_corretos(s):
            return True
        else:
            return False

def comeca_com_2letras(s):
    if s[:2].isalpha():
        return True
    else:
        return False

def tamanho_valido(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def caracteres_corretos(s):
    if s.isalnum():
        return True
    else:
        return False

def numeros_corretos(s):
    n = ''
    for l in s:
        if l.isdigit():
            n += l
    if n[0] == '0':
        return False
    else:
        if s.endswith(n):
            return True
        else:
            return False

if __name__ == "__main__":
    main()