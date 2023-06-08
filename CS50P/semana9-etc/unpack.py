def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**), "Knuts")

# x = {"x":2, "y":3, "z":5}
a, b, c = {"x":2, "y":3, "z":5}.values()

print(a, b, c)
# print(x)