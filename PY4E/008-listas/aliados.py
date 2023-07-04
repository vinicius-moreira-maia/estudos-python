a = [1,2,3]
b = a

a[0] = 555

print(a)
print(b)
print(b is a) # True

print('------')

x = 0
y = x
print(x is y) # True

x = 1 # instanciação de um novo objeto para x, y permanece 0

print(x)
print(y)
print(x is y) # False