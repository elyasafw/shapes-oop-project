from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side):
        self.valid_parameters(side)
        super().__init__(side, side)
        self.side = side

    def get_area(self):
        return self.side * self.side
    
    def get_perimeter(self):
        return 4 * self.side