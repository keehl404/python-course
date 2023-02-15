from src.Rectangle import Rectangle


class TestRectangle:
    def test_create_rectangle(self):
        rectangle = Rectangle(4, 5)
        assert isinstance(rectangle, Rectangle)
        assert rectangle.name == "Rectangle"
        assert rectangle.side_a == 4
        assert rectangle.side_b == 5

    def test_perimeter_rectangle(self):
        rectangle = Rectangle(4, 5)
        assert rectangle.perimeter == 18

    def test_area_rectangle(self):
        rectangle = Rectangle(4, 5)
        assert rectangle.area == 20

    def test_add_area_to_rectangle(self):
        rectangle1 = Rectangle(4, 5)
        rectangle2 = Rectangle(5, 4)
        assert rectangle1.add_area(rectangle2) == 40
