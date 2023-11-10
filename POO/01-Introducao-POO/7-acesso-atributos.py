'''
privado -> acessível apenas na classe de definição
protegido -> acessível em "certos casos" (subclasses por exemplo)
público -> acessível livremente

name -> público
_name -> protegido
__name -> privado
'''

class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"


x = A()
print(x.pub)
print(x._prot)
# print(x.__priv) # ERRO