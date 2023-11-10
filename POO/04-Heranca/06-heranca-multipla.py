# Herança Múltipla
# superclasse = base class (classe base)

class A:
    def m(self):
        print("m of A called")
class B(A):
    #def m(self):
     #   print("m of B called")
    pass
class C(A):
    def m(self):
        print("m of C called")
class D(B, C):
    pass

if __name__ == "__main__":
   x = D()

   # o método chamado respeita a ordem da herança, que é da direita para a esquerda, ou seja, o método m() de C será chamado
   x.m()