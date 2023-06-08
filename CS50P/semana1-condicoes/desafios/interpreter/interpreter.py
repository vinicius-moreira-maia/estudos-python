s = input("Expression: ")

n1, op, n2 = s.split(" ")
n1 = int(n1)
n2 = int(n2)

match op:
    case "+":
        print(f"{n1 + n2:.1f}")
    case "-":
        print(f"{n1 - n2:.1f}")
    case "/":
        print(f"{n1 / n2:.1f}")
    case "*":
        print(f"{n1 * n2:.1f}")

