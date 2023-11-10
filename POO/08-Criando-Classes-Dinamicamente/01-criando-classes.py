x = 4
y = "xuxu"

# print(type(x), type("xuxu"))

# se eu usar type com o nome de uma classe, o retorno será sempre será que a classe é do tipo (ou classe) 'type'
# print(type(type(x)), type(type(y)))
# print(type(int))

class A:
    pass

# classes definidas (classes 'object') também são do tipo 'type'
# print(type(A))

# o fato de que classes são instâncias da classe 'type' nos permite a criação de metaclasses, que são classes que herdam da classe 'type'

# Metaclasse = subclasse da classe 'type'

# type() pode ser chamada com 3 parâmetros / se os 3 forem fornecidos ela retorna um novo tipo de objeto
# type(classname, superclasses, attributes_dict)

x = A()
print(type(x))

# criação de novo tipo com 'type'
B = type("B", (), {})
y = B()
print(type(y))

# quando se chama type(), o método __call__ de type é chamado (instâncias chamáveis) e executo dois outros métodos:
# type.__new__(typeclass, classname, superclasses, attributedict)
# type.__init__(cls, classname, superclasses, attributedict)

# o método __new__ cria e retorna um novo objeto classe, o __init__ inicializa o novo objeto criado