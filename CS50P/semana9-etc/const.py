class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS): # referância ao atributo global da classe
            print("meow")

cat = Cat()
cat.meow()

