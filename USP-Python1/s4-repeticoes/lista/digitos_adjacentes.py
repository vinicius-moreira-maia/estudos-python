num = input("Digite um número inteiro: ")

tem = False

for i in range(len(num) - 1):
    if num[i] == num[i + 1]:
        tem = True

if tem:
    print("sim")
else:
    print("não")
    
