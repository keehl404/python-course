from src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side, name="Square"):
        super().__init__(side, side, name)
