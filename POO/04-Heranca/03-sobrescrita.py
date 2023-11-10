# Sobrescrita

class Robot:
    def __init__(self, name):
        self.name = name
    
    def say_hi(self):
        print("Hi, I am " + self.name)


class PhysicianRobot(Robot):
    def say_hi(self):
        print("Everything will be okay! ") 
        print(self.name + " takes care of you!")


y = PhysicianRobot("James")

# método especializado
print("Método da classe:")
y.say_hi()

# método da superclasse
print("\nMétodo da superclasse:")
# passando a instância como parâmetro
Robot.say_hi(y)