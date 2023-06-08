from datetime import date
import re
import sys
import inflect

# não passou no último quesito (relacionado ao teste unitário)

def main():
    data = input("Date of Birth: ")

    # checa somente o formato, não os valores
    match = re.search(r"^(\d{4})-(\d{2})-(\d{2})$", data)

    if not match:
        sys.exit("Invalid date")

    ano = int(match.group(1))
    mes = int(match.group(2))
    dia = int(match.group(3))

    try:
        data_nascimento = date(ano, mes, dia)
    except ValueError:
        sys.exit("Invalid date")

    print(minutos_extenso(data_nascimento))

def minutos_extenso(data_nascimento):
    data_atual = date.today()

    # sobrecarga de operador via método __sub__ da classe 'date' (subtração de objetos)
    dif_data = data_atual - data_nascimento

    # total_seconds é método da classe 'timedelta', cuja instância é retornada pela subtração de objetos acima
    total_minutos = round(dif_data.total_seconds() / 60)

    p = inflect.engine()

    m = f"{p.number_to_words(total_minutos, andword = '')} minutes"
    m = m.capitalize()

    return m

if __name__ == "__main__":
    main()