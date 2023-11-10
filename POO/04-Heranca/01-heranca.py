# PEP 8 -> Toda comparação de tipos deve ser feita com isinstance(), e não com type()

class Robot:
    def __init__(self, name):
        self.name = name
      
    def say_hi(self):
        print("Hi, I am " + self.name)


class PhysicianRobot(Robot):
    pass


if __name__ == "__main__":

  x = Robot("Marvin")
  y = PhysicianRobot("James")

  # tanto x como y são instâncias de Robot (y também é pq é subclasse de Robot)
  print(isinstance(x, Robot), isinstance(y, Robot))

  # mas x não é instância da subclasse só por ser instância da superclasse
  print(isinstance(x, PhysicianRobot))
  
  print(isinstance(y, PhysicianRobot))

  # type() apenas retorna o tipo específico da classe, no caso y é instância de ambas, mas no primeiro caso dá False
  print(type(y) == Robot, type(y) == PhysicianRobot)