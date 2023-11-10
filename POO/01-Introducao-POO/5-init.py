# __init__ é um dos 'magic methods'.
class A:
    def __init__(self):
        print("obj A criado")

# x = A()

class Pessoa:
    def __init__(self, nome = None):
        self.nome = nome
    
    def diga_oi(self):
        if self.nome:
            print(f"oi, {self.nome}")
        else:
            print("tem ninguém com esse nome aqui não")

p = Pessoa()
p.diga_oi()

p2 = Pessoa("Jurupinga")
p2.diga_oi()