class Student:
    def __init__(self, nome, bairro):
        self.nome = nome # mesmo aqui o método setter é chamado
        self.bairro = bairro # mesmo aqui o método setter é chamado

    def __str__(self):
        return f"{self.nome} de {self.bairro}"

    @classmethod # -> método que pode ser chamado sem necessidade de instanciar um objeto
    def get(cls):
        nome = input("Nome: ")
        bairro = input("Bairro: ")
        return cls(nome, bairro) # retorna o objeto instanciado

    # método getter
    @property
    def bairro(self):
        return self._bairro

    # método getter
    @property
    def nome(self):
        return self._nome

    # método setter
    @bairro.setter
    def bairro(self, bairro):
        if bairro not in ["Messejana", "Aldeota", "Parangaba"]:
            raise ValueError("bairro inválido")
        self._bairro = bairro

    # método setter
    @nome.setter
    def nome(self, nome):
        if not nome:
            raise ValueError("nome inválido")
        self._nome = nome

def main():
    # get é um método de classe que fornece os inputs para que o usuário entre com os dados e, então, retorne um objeto instanciado
    student = Student.get()
    # infelizmente isso é possível
    student._nome = "Diego"
    print(student)

if __name__ == "__main__":
    main()

