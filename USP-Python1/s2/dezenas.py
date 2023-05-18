n = input("Digite um número inteiro: ")

if len(n) <= 2:
    print(f"O dígito das dezenas é {int(n) // 10}")
else:
    print(f"O dígito das dezenas é {int(n[len(n) - 2 :]) // 10}")