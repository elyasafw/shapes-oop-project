from calculator import Shape


class Square(Shape):
    def __init__(self, shape_type, side):
        super().__init__(shape_type)
        self.side = side

    def get_area(self):
        return self.side * self.side
    
    def get_perimeter(self):
        return 4 * self.side