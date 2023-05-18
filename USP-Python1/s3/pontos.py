x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

exp = (x1 - x2) ** 2 + (y1 - y2) ** 2

# elevar a 1/2 é tirar a raíz quadrada
dist = exp ** (1/2)

if dist >= 10:
    print("longe")
else:
    print("perto")