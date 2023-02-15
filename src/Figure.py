class Figure:
    def __init__(self, side, name=None):
        if self.__class__ == Figure:
            raise Exception("Невозможно создать класс")
        self.name = name
        self.side = side

    @property
    def perimeter(self):
        pass

    @property
    def area(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Это не фигура!")
        return self.area + figure.area
