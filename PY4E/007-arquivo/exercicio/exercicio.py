'''
output: Average spam confidence: 0.7507185185185187
'''
total = 0
linhas = 0

fname = input("Enter file name: ")

fh = open(fname)

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        linhas += 1
        i = line.index("0")
        num = float(line[i:])
        total += num

print("Average spam confidence:", total / linhas)

