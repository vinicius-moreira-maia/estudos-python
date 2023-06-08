# talvez usar sempre type hints seja uma boa prática

def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
miaus: str = meow(number)
print(miaus, end = "")