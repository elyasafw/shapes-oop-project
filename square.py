from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, shape_type, side):
        super().__init__(shape_type, side, side)
        self.side = side 