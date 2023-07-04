hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

def computepay(h, r):
    if h > 40:
        dif = h - 40
        add = dif * r * 1.5
        return 40 * r + add
    else:
        return h * r

p = computepay(hrs, rate)

print("Pay", p)