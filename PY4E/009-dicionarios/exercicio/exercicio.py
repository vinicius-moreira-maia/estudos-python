'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

OUTPUT ->cwen@iupui.edu 5
'''

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

cont = {}
for line in handle:
    if not line.startswith('From '):
        continue
    else:
        words = line.strip().split()
        if words[1] not in cont:
            cont[words[1]] = 1
        else:
            cont[words[1]] += 1

# total = max(cont.values())

maior = -1
eml = None
for email, qtd in cont.items():
    if qtd is None or qtd > maior:
        maior = qtd
        eml = email

print(eml, maior)