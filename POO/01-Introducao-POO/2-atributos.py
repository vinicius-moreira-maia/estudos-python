class Robot:
    pass


if __name__ == "__main__":
    x = Robot()
    y = Robot()

    # É possível também adicionar atributos de forma dinâmica nas classes, isso cria um atributo de classe.
    Robot.name = "Miguel"

    print(x.name, y.name)

    x.name = "Droid"

    print(x.name, y.name, Robot.name)
    print(x.__dict__, y.__dict__)
    print(Robot.__dict__)

    # Em resumo, quando digo x.name o Python procura esse atributo primeiro em x.__dict__, caso não haja, ele procura em Robot.__dict__. Caso não exista em nenhum, uma exceção será levantada (AttributeError).

    # Esse método faz com que a exceção não seja levantada, se eu fornecer um valor default.
    print(getattr(x, 'telefone', -1))


   