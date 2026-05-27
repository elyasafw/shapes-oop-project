from calculator import Shape
from math import pi


class Circle(Shape):
    def __init__(self, shape_type, radius):
        super().__init__(shape_type)
        self.radius = radius

    def get_area(self):
        return pi * self.radius
    
    def get_perimeter(self):
        return 2 * pi * self.radius