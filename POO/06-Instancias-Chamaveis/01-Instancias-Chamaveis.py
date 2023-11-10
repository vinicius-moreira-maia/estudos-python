# Instâncias chamáveis são quando objetos que não foram definidos como funções (métodos) podem ser chamados como tal

# toda função (método) em Python é uma instância chamável

# para checar se um objeto é chamável basta utilizar a função callable()

# para definir um objeto não chamável como chamável, deve-se implementar o método mágico __call__()

def oi():
    return "Zé"

class C:
    def __call__(self):
        return "É o brinca não, hein!"

if __name__ == "__main__":
    #x = 9
    #print(callable(x))
    #print(callable(oi))

    x = C()

    print(x())