from shape import Shape, math


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, None)

    def area(self):
        return round(math.pi * ((self.width / 2) ** 2))
