'''
def oi(obj):
    print(f"oi, {obj.nome}")

class Pessoa:
    pass

x = Pessoa()
x.nome = "Zé"
oi(x)
'''

# Não é boa prática, mas é possível incluir métodos em classes de forma dinâmica também.
def oi(obj):
    print(f"oi, {obj.nome}")

class Pessoa:
    # Se diga_oi recebe um método, então ele é método.
    diga_oi = oi

x = Pessoa()
x.nome = "Zé"
Pessoa.diga_oi(x)

# Método é apenas uma função definida em uma classe, cujo primeiro parâmetro é sempre uma refrência para a instância que está chamando o método ('self' é apenas uma convenção) -> ele é passado automaticamente.