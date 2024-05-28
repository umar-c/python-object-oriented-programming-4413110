# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints
from abc import ABC, abstractmethod
from math import pi

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return pi * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side ** 2
    
class Rectangle(GraphicShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calcArea(self):
        return self.width * self.height

#g = GraphicShape()

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
r = Rectangle(12, 14)
print(r.calcArea())
