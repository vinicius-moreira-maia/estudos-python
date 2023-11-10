# É possível inserir atributos em qualquer instância de classe, inclusive em funções.
# Funções no Python são objetos de primeira classe, assim como inteiros, e podem ser passadas como parâmetro, ser atribuídas a outras variáveis, etc.

def f(x):
    return x + 3

f.a =  "xuxu"
print(f.a)

def f1(x=""):
    # Na primeira vez que a função for chamada, o atributo será criado e 1 será adicionado, nas outras vezes o valor será incrementado.
    f1.cont = getattr(f1, "cont", 0) + 1
    return "Bora Biu !!!"

for _ in range(23):
    f1()

print(f1.cont)