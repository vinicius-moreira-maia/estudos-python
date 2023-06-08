import random

class Bairro:
    bairros = ["Messejana", "Aldeota", "Parangaba"]

    @classmethod
    def sort(cls, nome):
        print(f"{nome} mora no bairro {random.choice(cls.bairros)}")

Bairro.sort("Zé")
