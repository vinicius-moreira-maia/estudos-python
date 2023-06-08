class Rectangle:
    def __init__(self, width, height):
        self.width = width # setter method
        self.height = height # setter method

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, w):
        self._width = w

    @height.setter
    def height(self, h):
        self._height = h

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def get_diagonal(self):
        return round(((self.width ** 2 + self.height ** 2) ** .5), 2)

    def get_shape_image(self):
        for _ in range(self.height):
            print('*' * self.width)
        print()

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f'Square(side={self.width})'
