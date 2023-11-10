# o python já é uma linguagem polimórfica, por ser dinamicamente tipada

def f(x, y):
    print(x, y)

f(1, 2)
f(1.1, 2.3)
f('xuxu', 'zézé')

# em linguagens como java e c++ eu teria que criar vários métodos em sobrecarga