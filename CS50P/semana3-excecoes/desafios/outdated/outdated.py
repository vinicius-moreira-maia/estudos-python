meses = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        data = input("Date: ").strip()
        
        # lidando com as possíveis exceções durante a validação
        try:
            if formato_valido(data):
                print(converte_data(data))
                exit()
        except ValueError:
            pass

def formato_valido(data):
    if "/" not in data:
        mes, dia, ano = data.split()
        if mes not in meses:
            return False
        elif not 31 >= int(dia[:-1]) >= 1 or dia[-1] != ",":
            return False
        elif len(ano) != 4:
            return False
        else:
            return True
    else:
        mes, dia, ano = data.split("/")
        if int(mes) > 12 or int(mes) < 1:
            return False
        elif not 31 >= int(dia) >= 1:
            return False
        elif len(ano) != 4:
            return False
        else:
            return True

def converte_data(data):
    dt = ""
    if "/" not in data:
        mes, dia, ano = data.split()

        if meses.index(mes) + 1 < 10:
            mes = "0" + str(meses.index(mes) + 1)
        else:
            mes = str(meses.index(mes) + 1)

        if int(dia[:-1]) < 10:
            dia = "0" + dia[:-1]
        else:
            dia = dia[:-1]

        dt = ano + "-" + mes + "-" + dia
        return dt
    else:
        mes, dia, ano = data.split("/")

        if int(mes) < 10:
            mes = "0" + mes
        else:
            pass

        if int(dia) < 10:
            dia = "0" + dia
        else:
            pass

        dt = ano + "-" + mes + "-" + dia
        return dt

main()