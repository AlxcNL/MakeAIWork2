from rectangle import Rectangle
from triangle import Triangle
from circle import Circle

rectangle = Rectangle(4, 5)
print(f"The area of the rectangle is : {rectangle.area}")

triangle = Triangle(4, 5)
print(f"The area of the triangle is : {triangle.area}")

circle = Circle(4)
print(f"The area of the triangle is : {circle.area()}")
