class Wizard:
    def __init__(self, nome):
        if not nome:
            raise ValueError("nome não informado")
        self.nome = nome
    ...

# classe que herda da classe Wizard
class Student(Wizard):
    def __init__(self, nome, house):
        super().__init__(nome) # executa o método construtor da superclasse
        self.house = house
    ...

# classe que herda da classe Wizard
class Professor(Wizard):
    def __init__(self, nome, subject):
        super().__init__(nome) # executa o método construtor da superclasse
        self.subject = subject
    ...

wizard = Wizard("Albus")
student = Student("Harry", "Grifinória")
professor = Professor("Severus", "Defesa contra magia negra")