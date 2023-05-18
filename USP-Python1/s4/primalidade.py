n = int(input("Digite um número inteiro: "))

primo = True

if n > 2:
    for i in range(2, n):
        if n % i == 0:
            primo = False

if primo:
    print("primo")
else:
    print("não primo")

