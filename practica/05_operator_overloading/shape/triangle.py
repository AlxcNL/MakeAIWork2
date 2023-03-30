from shape import Shape
from shape import math


class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return round(0.5 * self.width * self.height)
