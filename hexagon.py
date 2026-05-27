from calculator import Shape
from math import sqrt


class hexagon(Shape):
    def __init__(self, shape_type, side):
        super().__init__(shape_type)
        self.side = side

    def get_area(self):
        return (3 * sqrt(3) * self.side**2) / 2
    
    def get_perimeter(self):
        return 6 * self.side