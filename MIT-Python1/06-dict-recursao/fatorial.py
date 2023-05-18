def main():
    print(fat_loop(4))
    print(fat_rec(4))

def fat_loop(n):
    res = 1
    while n > 1:
        res *= n
        n -=1
    return res

def fat_rec(n):
    if n == 1:
        return 1
    return n * fat_rec(n - 1)

if __name__ == "__main__":
    main()