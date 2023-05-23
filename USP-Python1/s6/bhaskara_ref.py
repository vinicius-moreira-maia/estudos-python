# refatorar é tornar um código mais legível, modularizado e escalável

def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    imprime_raizes(a, b, c)

def delta(a, b, c):
    return b ** 2 - 4 * a * c

def imprime_raizes(a, b, c):
    d3lta = delta(a, b, c)

    if d3lta < 0:
        print("esta equação não possui raízes reais")
    elif d3lta == 0:
        print(f"a raiz dupla desta equação é {bhaskara(d3lta, b, a)}")
    else:
        x1, x2 = bhaskara(d3lta, b, a)

        if x1 >= x2:
            print(f"as raízes da equação são {x2} e {x1}")
        else:
            print(f"as raízes da equação são {x1} e {x2}")

def bhaskara(d3lta, b, a):
    if d3lta < 0:
        return None
    
    x1 = ((-1 * b) + (d3lta ** (1/2))) / 2 * a
    x2 = ((-1 * b) - (d3lta ** (1/2))) / 2 * a

    if d3lta == 0:
        return x1
    else:
        return (x1, x2)

if __name__ == "__main__":
    main()