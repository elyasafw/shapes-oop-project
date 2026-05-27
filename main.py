from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle
from hexagon import Hexagon


rectangle_1 = Rectangle("rectangle_1", 10, 40)
rectangle_2=  Rectangle("rectangle_2", 7, 0)
square_1 = Square("square_1", 40)
square_2 = Square("square_2", 8)
triangle_1 = Triangle("triangle_1", 10, 4, 6, 8, 21)
triangle_2 = Triangle("triangle_2", 24, 13, -5, 9, 71)
circle_1 = Circle("circle_1", 35)
circle_2 = Circle("circle_2", 17)
hexagon_1 = Hexagon("hexagon_1", 68)
hexagon_2 = Hexagon("hexagon_2", -40)

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

for i in shape_list:
    print(i)