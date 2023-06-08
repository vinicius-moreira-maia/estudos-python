import re

url = input("URL: ").strip()

usuario = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"usuario: {usuario}")