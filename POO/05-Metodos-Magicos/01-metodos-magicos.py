# métodos mágicos -> existe um método mágico para todos os operadores do Python (+, -, * ...)
# métodos mágicos são métodos de nomes definidos que não precisam ser explicitamente invocados para serem usados

'''
- expressão -> x + y
- x como instância de K
- o Python procura na definição da classe K o método __add__
- se existir esse método o Python executa: x.__add__(y)
- caso não ache o método, a exceção TypeError será levantada
- para todo operador existe um método mágico, e a sintaxe geral é a seguinte: objeto.__metodo__(self, other) ou objeto.__metodo__(self)
- a forma de usar é sobrescrevendo o método mágico
'''

class Tamanho:
  __medidas = {"mm" : 0.001, "cm" : 0.01, "m" : 1, "km" : 1000,
                "in" : 0.0254, "ft" : 0.3048, "yd" : 0.9144,
                "mi" : 1609.344}

  def __init__(self, valor, unidade = "m"):
    self.valor = valor
    self.unidade = unidade

  def converter_para_metros(self):
    return self.valor * Tamanho.__medidas[self.unidade]

  def __add__(self, other):
    if type(other) == int or type(other) == float:
        # para que seja possível coisas do tipo Tamanho(2) + 2.5
        t = self.converter_para_metros() + other
    else:
        t = self.converter_para_metros() + other.converter_para_metros()
    return Tamanho(t / Tamanho.__medidas[self.unidade], self.unidade)

  def __str__(self):
    return str(self.converter_para_metros())

  # __repr__ retorna uma string que pode ser lida como um comando
  def __repr__(self):
    return "Tamanho(" + str(self.valor) + ", '" + self.unidade + "')"

  # __iadd__ sobrescreve o operador +=
  def __iadd__(self, other):
    if type(other) == int or type(other) == float:
        # para que seja possível coisas do tipo Tamanho(2) + 2.5
        t = self.converter_para_metros() + other
    else:
        t = self.converter_para_metros() + other.converter_para_metros()
    self.valor = t / Tamanho.__medidas[self.unidade]
    return self

  # __radd__ aqui é como um complemento para a função __add__ / add lida com a adição de valores da esquerda para a direita, radd faz o oposto
  def __radd__(self, other):
    return Tamanho.__add__(self, other)


if __name__ == "__main__":
  x = Tamanho(4)
  print(x)
  y = eval(repr(x))
  z = Tamanho(4.5, "yd") + Tamanho(1)
  print(repr(z))
  print(z)

  x += Tamanho(1)
  x += Tamanho(4, "yd")

  x += 1
  print(x)