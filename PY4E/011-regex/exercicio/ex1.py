import re

def main():
    total = retorna_soma("regex_sum_1688580.txt")
    print(total)
    
def retorna_soma(filename):
    total = 0
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            num = re.findall(r"\d+\.?\d*", line)
            if len(num) > 0:
                for n in num:
                    total += float(n)
    return total

if __name__ == "__main__":
    main()