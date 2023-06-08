import re

nome = input("nome: ").strip()

# operador 'walrus'
if match := re.search(r"^(.+), *(.+)$", nome):
    nome = f"{match.group(2)} {match.group(1)}"

print(f"hello, {nome}")