import re

email = input("email: ").strip()

if re.search(r'^\w+@\w+\.(com|edu|gov|net|org)$', email):
    print("valid")
else:
    print("invalid")