menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    pedidos()

def pedidos():
    total = 0.0
    total_saida = None
    while True:
        try:
            pedido = input('Item: ').strip().title()
            total += menu[pedido]
        except EOFError:
            print()
            exit()
        except KeyError:
            pass
        else:
            total_saida = total
            print(f"Total: ${total_saida:.2f}")

main()