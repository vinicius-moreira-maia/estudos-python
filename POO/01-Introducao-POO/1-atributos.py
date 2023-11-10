'''
Propriedades e atributos são diferentes em Python, mas podem ser sinônimos em outros casos.
'''


# Toda classe criada herda de outras classes do próprio Python.
class Robot:
    pass


if __name__ == "__main__":
    x = Robot()
    y = Robot()

    # Objetos aliados (nomes com as mesmas referências).
    y2 = y 

    print(x is y)
    print(y is y2)

    # É possível criar atributos de forma dinâmica, mas isso afeta somente este objeto, e não a classe Robot.
    x.name = "XYZ"
    x.idade = 22

    print(x.name, x.idade)
    # print(y.name, y.idade) ERRO

    # Todo objeto armazena um par chave-valor de seus atributos no dicionário __dict__.
    print(x.__dict__)
    print(y.__dict__)