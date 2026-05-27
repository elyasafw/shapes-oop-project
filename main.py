from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle
from hexagon import Hexagon


rectangle_1 = Rectangle(10, 40)
rectangle_2=  Rectangle(7, 10)
square_1 = Square(40)
square_2 = Square(8)
triangle_1 = Triangle(10, 4, 6, 8, 21)
triangle_2 = Triangle(24, 13, 5, 9, 71)
circle_1 = Circle(7)
circle_2 = Circle(7)
hexagon_1 = Hexagon(68)
hexagon_2 = Hexagon(40)

shape_list = [
    rectangle_1,
    rectangle_2,
    square_1,
    square_2,
    triangle_1,
    triangle_2,
    circle_1,
    circle_2,
    hexagon_1,
    hexagon_2
    ]

try:
    for i in shape_list:
        print(i)
except (ValueError, TypeError) as e:
    print(e)

print(repr(triangle_1))