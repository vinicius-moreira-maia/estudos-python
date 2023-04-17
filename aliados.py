a = [11, 22, 33]
b = [44, 55, 66]
c = ['oi', 'zé']

a.append(c)

print(a)

c.append(b)

print(a)

a[3][2][0] = 'dudu'

print(a)
print(b)