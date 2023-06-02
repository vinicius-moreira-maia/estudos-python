class Triangulo():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def perimetro(self):
        return self.a + self.b + self.c


    def tipo_lado(self):
        if self.a == self.b and self.b != self.c:
            return 'isósceles'
        
        if self.a == self.c and self.c != self.b:
            return 'isósceles'
    
        if self.a == self.b and self.b == self.c:
            return 'equilátero'
        
        if self.a != self.b and self.b != self.c:
            return 'escaleno'


def main():
    t = Triangulo(4, 4, 4)
    print(t.tipo_lado())

    u = Triangulo(3, 4, 5)
    print(u.tipo_lado())

if __name__ == '__main__':
    main()