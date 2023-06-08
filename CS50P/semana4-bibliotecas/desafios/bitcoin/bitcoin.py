import sys
import requests
import json

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        nbitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        # utilizando um webservice através de uma API (:
        request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Error on the request")

    # print(json.dumps(request.json(), indent = 2))

    try:
        result = request.json() # json convertido para estrutura de dados do Python
    except requests.exceptions.JSONDecodeError:
        sys.exit("Error on the JSON decoder")

    current = string_to_float(result["bpi"]["USD"]["rate"])
    total = nbitcoins * current

    print(f"${total:,.4f}")

def string_to_float(s):
    s = list(s)
    s.remove(",")
    s = ''.join(s)
    return float(s)

if __name__ == "__main__":
    main()