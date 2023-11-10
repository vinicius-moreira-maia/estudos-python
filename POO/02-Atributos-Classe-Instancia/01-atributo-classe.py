class C: 
    # atributo de classe
    # pode ser acessado tanto via classe como via instância
    # para ser alterado deve ser acessado somente pela classe
    # se for alterado por instância um novo atributo de instância será criado
    __counter = 0

    def __init__(self): 
        type(self).__counter += 1
    
    def __del__(self):
        type(self).__counter -= 1

    # métodos estáticos não estão atrelados nem à classe ou à instância, mas ainda assim podem acessar qualquer atributo ou método privado da classe
    @staticmethod
    def CInstances():
        return C.__counter

    # métodos de classe estão atrelados à classe, e recebem a referência 'cls'
    @classmethod
    def CInstances_2(cls):
        return cls.__counter

    
if __name__ == "__main__":
    x = C()
    print("Number of instances: : " + str(x.CInstances_2()))
    
    y = C()
    print("Number of instances: : " + str(y.CInstances()))
    