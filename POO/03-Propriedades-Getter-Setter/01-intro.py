# Propriedades são implementadas em C

# Foi mostrada a simulação da implementação de propriedades customizadas usando Python através de descriptores

# Descriptores são atributos de objetos que possuem comportamento atrelado em suas definições. Esses comportamentos são acionados quando se acessa os atributos (descriptores). Para um objeto ser descriptor ele precisa sobrescrever um dos 3 métodos: __get__(), __set__() ou __delete__().


'''
-> O jeito "pythônico" de lidar com atributos, getters e setters.

- Se o atributo precisa ser acessado fora da classe, então deve ser público. (self.x)

- Se não precisa ser acessado, então deve ser privado. (self.__x)

- Atributos privados com getters e setters devem ser usados somente quando alguma checagem de valor ou transformações nos dados precisarem ser feitas.

- O jeito Python de criar getters e setters é através de propriedades.

- Propriedades (getters e setters) podem ser criadas para qualquer atributo SEM alterar a interface da classe. Usando getters e setters a interface seria alterada.
'''


class P:
    def __init__(self, x):
        # aqui o método setter já está sendo usado
        self.x = x 
    
    # definindo o atributo __x como propriedade (por conta dos decoradores, é possível haver 2 métodos de mesmo nome, caso contrário daria erro, pois em Python não existe sobrecarga de métodos)

    # getter
    @property
    def x(self):
        return self.__x
    
    # setter
    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

xuxu = P(36)

# método getter sendo usado
print(xuxu.x)

# método setter sendo usado
xuxu.x = 100

# método getter sendo usado
print(xuxu.x)