import re

x = open('mbox.txt')

for line in x:
    if not line.startswith('From: '):
        continue
    line = line.strip()
    email = re.search(r'^From: .+@([a-z]+)\..+$',line)
    org = email.group(1)
    print(org)
