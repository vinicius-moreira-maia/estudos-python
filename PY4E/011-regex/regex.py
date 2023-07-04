import re

file = open("mbox-short.txt")

for line in file:
    line = line.strip()
    # print(line)
    email = re.findall("[a-zA-Z0-9]\S+@\S+[a-zA-Z0-9]", line)
    if len(email) > 0:
        print(email)
