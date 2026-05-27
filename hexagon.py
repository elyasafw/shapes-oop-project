from calculator import Shape
from math import sqrt


class Hexagon(Shape):
    def __init__(self, side):
        self.valid_parameters(side)
        super().__init__()
        self.side = side

    def get_area(self):
        return (3 * sqrt(3) * self.side**2) / 2
    
    def get_perimeter(self):
        return 6 * self.side