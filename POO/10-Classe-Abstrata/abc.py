# ABC = Abstract Base Class
# Classes abstratas são classes que contém um ou mais métodos abstratos, que são apenas a assinatura de métodos
# Classes abstratas não podem ser instanciadas
# Requerem subclasses para implementar seus métodos
# O Python não suporta classes abstratas nativamente, mas oferece o módulo ABC

from abc import ABC, abstractmethod

class ClasseAbstrata(ABC):
    def __init__(self, nome):
        self.nome = nome
        super().__init__()
    
    @abstractmethod
    def oi(self):
        print("Oi UNIVERSOOOOOO")
        pass

class Terra(ClasseAbstrata):
    def oi(self):
        # métodos abstratos da classe abstrata podem conter implementação, e podem ser chamados com super()
        super().oi()
        print(f"oi, {self.nome}, bem vindo a Terra!")

class Marte(ClasseAbstrata):
    def oi(self):
        super().oi()
        print(f"oi, {self.nome}, bem vindo a Marte!")

# as subclasses de uma classe abstrata não podem ser instanciadas se não sobrescreverem todos os métodos da classe abstrata
x = Terra("Xiríudes")
y = Terra("Bombom")

x.oi()
y.oi()