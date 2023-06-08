class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("numero invalido")
        self._capacity = capacity # '_capacity', pois não defini um setter pra esse atributo
        self.biscoitos = 0

    def __str__(self):
        return '🍪' * self.biscoitos # getter

    def deposit(self, n):
        if self.biscoitos + n > self.capacity:
            raise ValueError("nao cabe mais biscoito")
        else:
            # setter         # getter
            self.biscoitos = self.biscoitos + n

    def withdraw(self, n):
        if n > self.biscoitos:
            raise ValueError("nao tem esse tanto de biscoito")
        # setter         # getter
        self.biscoitos = self.biscoitos - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def biscoitos(self):
        return self._biscoitos

    @biscoitos.setter
    def biscoitos(self, n):
        self._biscoitos = n

    @property
    def size(self):
        return self.biscoitos

def main():
    jar = Jar(10)
    print(jar) # pote vazio

    jar.deposit(5)
    print(jar)

    jar.withdraw(3)
    print(jar)

    print(jar.size)

if __name__ == "__main__":
    main()

