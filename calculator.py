class Shape:
    def __init__(self):
        pass

    @staticmethod
    def valid_parameters(*values):
        for v in values:
            if not isinstance(v, (int, float)) or isinstance(v, bool):
                raise(TypeError("Invalid parameter... Dimensions should only be numbers"))
            elif v <= 0:
                raise(ValueError("Invalid parameter... Dimensions must be greater than 0"))

    def get_area(self):
        pass

    def get_perimeter(self):
        pass
    
    def __str__(self):
        return f"Shape: {self.__class__.__name__} | Area = {self.get_area()} | Perimeter = {self.get_perimeter()}"
    
    def __repr__(self):
        attrs = [f"{k} = {repr(v)}" for k, v in self.__dict__.items()]
        attrs_string = ", ".join(attrs)
        return f"{self.__class__.__name__}: ({attrs_string})"