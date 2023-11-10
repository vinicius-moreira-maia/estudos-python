from itertools import chain
import random
# o método random.uniform(x, y) retorna um real entre x e y, x e y inclusos

class Robo:
    # atributos de instância (privados)
    __nomes_ilegais = {"R2D2", "Megazord"}
    __nivel_de_saude_critico = 0.6

    def __init__(self, nome):
        self.nome = nome # uso do método setter
        self.nivel_de_saude = random.random()

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        # fazendo referência ao atributo de classe
        if nome in Robo.__nomes_ilegais:
            self.__nome = "JoãoDROID"
        else:
            self.__nome = nome
    
    # o método __str__ sobrepõe a saída padrão do objeto na função print()
    def __str__(self):
        # self.nome aqui é o getter
        return f"{self.nome}, Robô"
    
    # __add__ é a definição do comportamento esperado para a adição de dois objetos
    def __add__(self, other):
        primeiro = self.nome.split("-")[0]
        segundo = other.nome.split("-")[0]
        # antes o retorno era Robot(f"{primeiro}-{segundo}"), com type(self) eu torno o método mais flexível, podendo também retornar objetos de subclasses
        return type(self)(f"{primeiro}-{segundo}")
    
    def precisa_de_enfermeira(self):
        if self.nivel_de_saude < Robo.__nivel_de_saude_critico:
            return True
        else:
            return False
    
    def diga_oi(self):
        print(f"Oi! Eu sou o {self.nome}!")
        print(f"Meu nível de saúde é: {self.nivel_de_saude}\n")


class RoboEnfermeiro(Robo):
    def __init__(self, nome = "Astolfo", poder_de_cura = None):
        super().__init__(nome)
        if poder_de_cura is None:
            self.poder_de_cura = random.uniform(0.8, 1)
        else:
            self.poder_de_cura = poder_de_cura
    
    def diga_oi(self):
        print(f"Calma rapazzzz, o dotô {self.nome} vai cuidar de tudo!")
    
    def diga_oi_pro_doutor(self):
        Robo.diga_oi(self)
    
    def curar(self, robo):
        if robo.nivel_de_saude > self.poder_de_cura:
            print(f"{self.nome} tá fraco demais pra curar o {robo.nome}")
        else:
            robo.nivel_de_saude = random.uniform(robo.nivel_de_saude, self.poder_de_cura)
            print(f"{robo.nome} foi curado pelo {self.nome}!")


class RoboLutador(Robo):
    __dano_maximo = 0.2

    def __init__(self, nome = "Van Damme", poder_de_luta = None):
        super().__init__(nome)
        if poder_de_luta:
            self.poder_de_luta = poder_de_luta
        else:
            dano_max = RoboLutador.__dano_maximo
            self.poder_de_luta = random.uniform(dano_max, 1)
    
    def diga_oi(self):
        print(f"Sou o {self.nome} e quebro todo mundo!!")
    
    def ataque(self, other):
        other.nivel_de_saude = other.nivel_de_saude * self.poder_de_luta
        if isinstance(other, RoboLutador):
            # o outro robô contra-ataca
            self.nivel_de_saude = self.nivel_de_saude * other.poder_de_luta


# herança múltipla
# o robô lutador e enfermeiro luta e cura =)))
class RoboEnfermeiroLutador(RoboEnfermeiro, RoboLutador):
    def __init__(self, nome, modo = "enfermeiro"):
        super().__init__(nome)
        self.modo = modo # o outro estado seria modo lutador

    def diga_oi(self):
        if self.modo == "lutador":
            RoboLutador.diga_oi(self)
        elif self.modo == "enfermeiro":
            RoboEnfermeiro.diga_oi(self)
        else:
            Robo.diga_oi(self)        

    
if __name__ == "__main__":
    '''
    primeira_geracao = (Robo("Betinho"), Robo("Doidona"), Robo("Biu"))
    ger1 = primeira_geracao

    bebes = [ger1[0] + ger1[1], ger1[1] + ger1[2]]
    bebes.append(bebes[0] + bebes[1])

    enfermeiros = [RoboEnfermeiro("Corrinha"), RoboEnfermeiro("Ednardo", poder_de_cura = 1)]

    for enf in enfermeiros:
        print("Poder de cura de " + enf.nome , enf.poder_de_cura)
    
    print(f"\nVamos começar a cura do Zé Gotinha!!!!!")

    # chain itera nas duas listas sem criar uma nova
    for robo in chain(ger1, bebes):
        robo.diga_oi()
        if robo.precisa_de_enfermeira():
            # escolha um enfermeiro aleatoriamente
            enf = random.choice(enfermeiros)
            enf.curar(robo)
            print(f"Novo nível de saúde: {robo.nivel_de_saude}")
        else:
            print(f"{robo.nome} já é MONSTRÃO!!!!")
        print()
    
    #x = enfermeiros[0] + enfermeiros[1]
    #x.diga_oi()
    #print(type(x))

    lutadores = (RoboLutador("Rambo", 0.4), RoboLutador("Jackie Chan", 0.2))
    
    print("Antes do pau quebrar:")
    for lutador in lutadores:
        enfermeiros[1].curar(lutador)
        print(lutador, lutador.nivel_de_saude, lutador.poder_de_luta)
    
    lutadores[0].ataque(lutadores[1])

    print("Depois do pau quebrar:")
    for lutador in lutadores:
        enfermeiros[1].curar(lutador)
        print(lutador, lutador.nivel_de_saude, lutador.poder_de_luta)
    '''

    le1 = RoboEnfermeiroLutador("Bozo", modo = "lutador")
    le2 = RoboEnfermeiroLutador("Beliza")

    if le1.precisa_de_enfermeira():
        le1.curar(le1)
    
    if le2.precisa_de_enfermeira():
        le2.curar(le2)
    
    print(le1.nivel_de_saude, le2.nivel_de_saude)

    le1.diga_oi()
    le2.diga_oi()
    le1.ataque(le2)
    print(le1.nivel_de_saude, le2.nivel_de_saude)