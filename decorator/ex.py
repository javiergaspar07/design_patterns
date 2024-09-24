from abc import ABC

class Shape(ABC):
    @property
    def name(self):
        return ''

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def name(self):
        return 'circle'

    def resize(self, factor):
        self.radius *= factor
    
    def __str__(self):
        return f"A {self.name} of radius {self.radius}"

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    @property
    def name(self):
        return 'square'
    
    def __str__(self):
        return f"A {self.name} with side {self.side}"

class ColoredShape:
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        return self.shape.resize(factor)

    def __str__(self):
        return f"{str(self.shape)} has the color {self.color}"


if __name__ == '__main__':
    circle = ColoredShape(Circle(5), 'red')
    
    print('A circle of radius 5 has the color red' == str(circle))
    circle.resize(2)
    print('A circle of radius 10 has the color red' == str(circle))
