import random

moeda = random.choice(["cara", "coroa"])
print(moeda)

num = random.randint(1, 10)
print(num)

j = ["Zidane", "Messi", "Ronaldo"]
random.shuffle(j)
for n in j:
    print(n)