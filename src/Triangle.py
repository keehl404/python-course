from src.Figure import Figure


class Triangle(Figure):
    def __new__(cls, *args):
        side_a, side_b, side_c = args
        if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
            return None
        return super().__new__(cls)

    def __init__(self, side_a, side_b, side_c, name="Triangle"):
        super().__init__(side_a, name)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def area(self):
        return self.area_formula(self.perimeter, self.side_a, self.side_b, self.side_c)

    @staticmethod
    def area_formula(perimeter, side_a, side_b, side_c):
        perimeter /= 2
        return (
            perimeter * (perimeter - side_a) * (perimeter - side_b) * (perimeter - side_c)
        ) ** 0.5
