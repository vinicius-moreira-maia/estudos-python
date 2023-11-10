# PEP 8 -> Toda comparação de tipos deve ser feita com isinstance(), e não com type()

class A:
    pass
class B(A):
    pass
class C(B):
    pass
  
x = C()

# não importa o número de superclasses, x será instância de todas
print(isinstance(x, A))