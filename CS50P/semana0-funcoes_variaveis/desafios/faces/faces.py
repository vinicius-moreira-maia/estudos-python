def main():
    s = input("")
    print(convert(s))

def convert(n):
    t = n.replace(":)","🙂").replace(":(","🙁")
    return t

main()