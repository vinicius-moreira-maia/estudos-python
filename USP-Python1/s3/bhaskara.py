a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    x = ((-1 * b) + (delta ** (1/2))) / 2 * a
    print(f"a raiz dupla desta equação é {x}")
else:
    x = ((-1 * b) + (delta ** (1/2))) / 2 * a
    y = ((-1 * b) - (delta ** (1/2))) / 2 * a

    if x >= y:
        print(f"as raízes da equação são {y} e {x}")
    else:
        print(f"as raízes da equação são {x} e {y}")