# todo objeto e classe possuem um dicionário __dict__ que armazena seus atributos

# slots são listas criadas para armazenar quais atributos existirão nas instâncias (não é sobre atributo de classe), e isso previne a adição dinâmica de atributos

class P:

    __slots__ = ['obj_attr']

    # inst_attr = 22

    def __init__(self):
        self.obj_attr = 14
        # self.y = 123 ERRO
    
    def get(self):
        return self.obj_attr

p = P()
print(p.obj_attr)

# p.nome = "zézé" ERRO

# atributos de classe podem ser adicionados
type(p).inst_attr = "xuxu"
print(type(p).inst_attr)

# rint(p.__dict__)

# métodos são atributos da classe
# print(type(p).__dict__)