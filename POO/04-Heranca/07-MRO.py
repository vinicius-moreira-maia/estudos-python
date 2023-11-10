# MRO (Method Resolution Order)

# em Python3.x, toda classe já herda de 'object', não preciso fazer isso manualmente
class A:
    def m(self):
        print("m of A called")
class B(A):
    def m(self):
        print("m of B called")
        super().m()
class C(A):
    def m(self):
        print("m of C called")
        super().m()
class D(B,C):
    def m(self):
        print("m of D called")
        super().m()

x = D()
# x.m()

# MRO é baseado no algoritmo  "C3 superclass linearisation", que lineariza a estrutura em árvore da hierarquia de classes para estabelecer a ordem de chamada dos métodos
print(D.mro())
print(B.mro())
print(A.mro())

# B.m(x)