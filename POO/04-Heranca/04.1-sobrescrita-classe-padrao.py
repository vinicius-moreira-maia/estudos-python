# classes padrão como classes base (superclasses)

class Lista(list):
  def __init__(self, l):
    list.__init__(self, l)

  def adiciona(self, valor):
    self.append(valor)


x = Lista([3, 5])
x.adiciona("xuxu")
print(x)