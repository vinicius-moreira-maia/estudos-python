s = int(input("Por favor, entre com o número de segundos que deseja converter: "))

m = s // 60
s = s - (m * 60)

h = m // 60
m = m - (h * 60)

d = h // 24
h = h - (d * 24)


print(f"{d} dias, {h} horas, {m} minutos e {s} segundos.")